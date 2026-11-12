<script>
  let dark = $state(true);

  $effect(() => {
    if (typeof document !== 'undefined') {
      document.documentElement.classList.toggle('dark', dark);
    }
  });
</script>

<button
  type="button"
  onclick={() => (dark = !dark)}
  aria-label={dark ? 'Switch to light mode' : 'Switch to dark mode'}
  class="fixed top-[1.125rem] right-[1.125rem] max-[520px]:top-3 max-[520px]:right-3
         w-[34px] h-[34px] flex items-center justify-center z-50
         bg-white dark:bg-[#1c1c1e]
         border border-[#d2d2d7] dark:border-[#38383a]
         text-[#6e6e73] dark:text-[#aeaeb2]
         hover:text-[#1d1d1f] dark:hover:text-[#f5f5f7]
         cursor-pointer transition-colors active:scale-95"
>
  {#if dark}
    <!-- Sun -->
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" stroke-linecap="round" aria-hidden="true">
      <circle cx="12" cy="12" r="4" />
      <line x1="12" y1="2" x2="12" y2="5" />
      <line x1="12" y1="19" x2="12" y2="22" />
      <line x1="4.22" y1="4.22" x2="6.34" y2="6.34" />
      <line x1="17.66" y1="17.66" x2="19.78" y2="19.78" />
      <line x1="2" y1="12" x2="5" y2="12" />
      <line x1="19" y1="12" x2="22" y2="12" />
      <line x1="4.22" y1="19.78" x2="6.34" y2="17.66" />
      <line x1="17.66" y1="6.34" x2="19.78" y2="4.22" />
    </svg>
  {:else}
    <!-- Moon -->
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor"
         stroke-width="2" stroke-linecap="round" aria-hidden="true">
      <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
    </svg>
  {/if}
</button>