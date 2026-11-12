<script>
  import CardHeader from './CardHeader.svelte';
  import UrlForm from './UrlForm.svelte';
  import ResultBlock from './ResultBlock.svelte';

  let shortUrl = $state('');
  let urlValid = $state(null);
  let loading = $state(false);
  let error = $state(null);

  let hasResult = $derived(shortUrl !== '');

  async function shorten(url) {
    if (loading || !url) return;

    loading = true;
    error = null;
    shortUrl = '';
    urlValid = null;

    try {
      const res = await fetch('http://localhost:8000/v1/sh', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url }),
      });

      if (res.status === 201) {
        const data = await res.json();
        shortUrl = data.url;
        urlValid = data.valid;
      } else if (res.status === 422) {
        const data = await res.json();
        const first = data?.detail?.[0];
        error = {
          kind: '422',
          message: first?.msg ?? 'Enter a valid URL (e.g. https://example.com).',
        };
      } else if (res.status === 500) {
        error = { kind: '500', message: 'Server error. Try again in a moment.' };
      } else {
        error = { kind: '500', message: `Unexpected response (${res.status}).` };
      }
    } catch {
      error = {
        kind: 'network',
        message: 'Could not reach the server. Check your connection.',
      };
    } finally {
      loading = false;
    }
  }
</script>

<article
  class="w-full max-w-[476px]
         bg-white dark:bg-[#1c1c1e]
         border border-[#d2d2d7] dark:border-[#38383a]
         shadow-[0_1px_2px_rgba(0,0,0,0.04),0_4px_20px_rgba(0,0,0,0.07)]
         dark:shadow-[0_1px_3px_rgba(0,0,0,0.5),0_8px_32px_rgba(0,0,0,0.45)]"
>
  <CardHeader />

  <div class="px-8 pt-[1.625rem] pb-8 flex flex-col gap-3.5
              max-[520px]:px-5 max-[520px]:pt-5 max-[520px]:pb-6">
    <UrlForm {loading} {error} onsubmit={shorten} />

    {#if hasResult}
      <ResultBlock {shortUrl} {urlValid} />
    {/if}
  </div>
</article>