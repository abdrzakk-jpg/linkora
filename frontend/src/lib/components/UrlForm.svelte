<script>
  let { loading, error, onsubmit } = $props();

  let inputUrl = $state('');
  let canSubmit = $derived(inputUrl.trim() !== '' && !loading);

  function handleSubmit() {
    if (canSubmit) onsubmit(inputUrl.trim());
  }

  function handleKeydown(e) {
    if (e.key === 'Enter') handleSubmit();
  }
</script>

<div class="flex flex-col gap-3.5">
  <div class="flex flex-col gap-[0.3rem]">
    <label for="url-input" class="text-xs font-normal tracking-[-0.008em] leading-none
                                   text-[#aeaeb2] dark:text-[#636366] select-none">
      URL to shorten
    </label>
    <input
      id="url-input"
      type="url"
      placeholder="https://example.com/very/long/path"
      bind:value={inputUrl}
      onkeydown={handleKeydown}
      disabled={loading}
      autocomplete="off"
      spellcheck="false"
      class="w-full h-11 px-3.5
             bg-white dark:bg-[#2c2c2e]
             border text-[15px] tracking-[-0.02em]
             text-[#1d1d1f] dark:text-[#f5f5f7]
             caret-[#5856d6] dark:caret-[#7d7aff]
             placeholder:text-[#aeaeb2] dark:placeholder:text-[#636366]
             outline-none transition-[border-color,box-shadow,background]
             focus:border-[#5856d6] dark:focus:border-[#7d7aff]
             focus:shadow-[0_0_0_2.5px_rgba(88,86,214,0.12)]
             dark:focus:shadow-[0_0_0_2.5px_rgba(125,122,255,0.15)]
             disabled:opacity-[0.45] disabled:cursor-not-allowed
             {error
               ? 'border-[#ff3b30] dark:border-[#ff453a] focus:!shadow-[0_0_0_2.5px_rgba(255,59,48,0.14)]'
               : 'border-[#d2d2d7] dark:border-[#38383a]'}"
    />
  </div>

  {#if error}
    <div role="alert"
         class="flex items-start gap-[0.45rem] px-3 py-2.5
                bg-[#fff5f5] dark:bg-[rgba(255,69,58,0.1)]
                border border-[rgba(255,59,48,0.25)] dark:border-[rgba(255,69,58,0.2)]
                text-[13px] leading-[1.45]
                text-[#ff3b30] dark:text-[#ff453a]">
      <svg width="13" height="13" viewBox="0 0 16 16" fill="none" aria-hidden="true"
           class="shrink-0 mt-[1px]">
        <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-width="1.5" />
        <line x1="8" y1="5" x2="8" y2="8.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
        <circle cx="8" cy="11" r="0.8" fill="currentColor" />
      </svg>
      <span>{error.message}</span>
    </div>
  {/if}

  <button
    type="button"
    onclick={handleSubmit}
    disabled={!canSubmit}
    aria-busy={loading}
    class="flex items-center justify-center gap-[0.45rem] w-full h-11 px-5
           bg-[#5856d6] dark:bg-[#7d7aff]
           enabled:hover:bg-[#3634c7] enabled:dark:hover:bg-[#9d9bff]
           text-white text-[15px] tracking-[-0.02em]
           cursor-pointer transition-[background-color,opacity,transform] duration-100
           active:scale-[0.97]
           disabled:opacity-[0.38] disabled:cursor-not-allowed"
  >
    {#if loading}
      <span class="w-[13px] h-[13px] shrink-0 rounded-full border-[1.75px]
                   border-white/30 border-t-white animate-spin
                   motion-reduce:animate-none motion-reduce:opacity-60"
            aria-hidden="true"></span>
      Shortening…
    {:else}
      Shorten URL
    {/if}
  </button>
</div>