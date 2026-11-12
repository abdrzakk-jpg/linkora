<script>
  import "../app.css"
  import ThemeToggle from '$lib/components/ThemeToggle.svelte';
  import ShortenerCard from '$lib/components/ShortenerCard.svelte';
</script>

<svelte:head>
  <title>Linkora</title>
  <meta name="description" content="Shorten any URL instantly." />
</svelte:head>

<ThemeToggle />

<div class="min-h-screen bg-[#f5f5f7] dark:bg-black text-[#1d1d1f] dark:text-[#f5f5f7] font-body transition-colors">
  <div class="min-h-screen flex items-center justify-center py-8 px-4
              max-[520px]:items-start max-[520px]:pt-14 max-[520px]:pb-4 max-[520px]:px-3">
    <ShortenerCard />
  </div>
</div>