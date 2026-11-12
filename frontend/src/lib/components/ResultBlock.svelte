<script>
  let { shortUrl, urlValid } = $props();

  let copied = $state(false);
  let copyTimer;

  async function copy() {
    if (!shortUrl) return;
    try {
      await navigator.clipboard.writeText(shortUrl);
      copied = true;
      clearTimeout(copyTimer);
      copyTimer = setTimeout(() => (copied = false), 2000);
    } catch {
      /* clipboard denied */
    }
  }

  function visit() {
    if (shortUrl) document.location.href = shortUrl.trim();
  }
</script>

<div class="flex flex-col gap-3 pt-2.5 border-t border-[#e8e8ed] dark:border-[#2c2c2e]"
     aria-live="polite">
  <!-- Validity row -->
  <div class="flex items-center justify-between gap-2">
    <span class="text-xs font-normal tracking-[-0.008em] text-[#aeaeb2] dark:text-[#636366]">
      Original URL
    </span>
    {#if urlValid === true}
      <span class="inline-flex items-center gap-[0.3rem] px-2 py-[0.2rem] rounded-[2px]
                   text-[11px] font-semibold tracking-[0.01em] leading-normal
                   bg-[#f0fff4] dark:bg-[rgba(48,209,88,0.1)]
                   text-[#34c759] dark:text-[#30d158]
                   border border-[rgba(52,199,89,0.25)] dark:border-[rgba(48,209,88,0.2)]">
        <span class="w-[5px] h-[5px] rounded-full shrink-0 bg-[#34c759] dark:bg-[#30d158]"></span>
        Reachable
      </span>
    {:else if urlValid === false}
      <span class="inline-flex items-center gap-[0.3rem] px-2 py-[0.2rem] rounded-[2px]
                   text-[11px] font-semibold tracking-[0.01em] leading-normal
                   bg-[#fffbeb] dark:bg-[rgba(255,214,10,0.08)]
                   text-[#f59e0b] dark:text-[#ffd60a]
                   border border-[rgba(245,158,11,0.25)] dark:border-[rgba(255,214,10,0.2)]">
        <span class="w-[5px] h-[5px] rounded-full shrink-0 bg-[#f59e0b] dark:bg-[#ffd60a]"></span>
        Unreachable
      </span>
    {/if}
  </div>

  <!-- Short URL + actions -->
  <div class="flex flex-col gap-[0.3rem]">
    <label for="short-out" class="text-xs font-normal tracking-[-0.008em] leading-none
                                   text-[#aeaeb2] dark:text-[#636366] select-none">
      Short link
    </label>
    <div class="flex gap-[0.375rem]">
      <input
        id="short-out"
        type="text"
        value={shortUrl}
        readonly
        tabindex="-1"
        class="flex-1 min-w-0 h-11 px-3.5
               bg-[#fafafc] dark:bg-[#252527]
               border border-[#e8e8ed] dark:border-[#2c2c2e]
               text-sm text-[#5856d6] dark:text-[#7d7aff]
               cursor-default overflow-hidden text-ellipsis whitespace-nowrap
               outline-none focus:border-[#d2d2d7] dark:focus:border-[#38383a] focus:shadow-none"
      />

      <button
        type="button"
        onclick={copy}
        aria-label={copied ? 'Copied!' : 'Copy link'}
        class="shrink-0 inline-flex items-center gap-[0.35rem] h-11 px-3.5 whitespace-nowrap
               text-[13px] tracking-[-0.012em] cursor-pointer
               transition-[background-color,color,border-color,transform] duration-100
               active:scale-95
               {copied
                 ? 'bg-[#f0fff4] dark:bg-[rgba(48,209,88,0.1)] border border-[rgba(52,199,89,0.25)] dark:border-[rgba(48,209,88,0.2)] text-[#34c759] dark:text-[#30d158]'
                 : 'bg-white dark:bg-[#2c2c2e] border border-[#d2d2d7] dark:border-[#38383a] text-[#6e6e73] dark:text-[#aeaeb2] hover:bg-[#e8e8ed] dark:hover:bg-[#2c2c2e] hover:text-[#1d1d1f] dark:hover:text-[#f5f5f7]'}"
      >
        {#if copied}
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true">
            <polyline points="2.5,8.5 6.5,12.5 13.5,4.5" stroke="currentColor"
                      stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" />
          </svg>
          Copied
        {:else}
          <svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true">
            <rect x="5.5" y="5.5" width="8" height="8" rx="1"
                  stroke="currentColor" stroke-width="1.4" />
            <path d="M3.5 10.5V3.5C3.5 2.94772 3.94772 2.5 4.5 2.5H11.5"
                  stroke="currentColor" stroke-width="1.4" stroke-linecap="round" />
          </svg>
          Copy
        {/if}
      </button>

      <button
        type="button"
        onclick={visit}
        class="shrink-0 inline-flex items-center gap-[0.35rem] h-11 px-3.5 whitespace-nowrap
               text-[13px] tracking-[-0.012em] cursor-pointer
               bg-white dark:bg-[#2c2c2e]
               border border-[#d2d2d7] dark:border-[#38383a]
               text-[#6e6e73] dark:text-[#aeaeb2]
               hover:bg-[#e8e8ed] dark:hover:bg-[#2c2c2e] hover:text-[#1d1d1f] dark:hover:text-[#f5f5f7]
               transition-[background-color,color,border-color,transform] duration-100
               active:scale-95"
      >
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden="true">
          <path d="M3 8H13M8.5 3.5L13 8L8.5 12.5" stroke="currentColor"
                stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
        visit
      </button>
    </div>
  </div>

  {#if urlValid === false}
    <p class="text-[13px] leading-normal tracking-[-0.01em] px-3 py-2.5
              text-[#f59e0b] dark:text-[#ffd60a]
              bg-[#fffbeb] dark:bg-[rgba(255,214,10,0.08)]
              border border-[rgba(245,158,11,0.25)] dark:border-[rgba(255,214,10,0.2)]">
      Link created — but the original URL appears unreachable.
      Double-check the address before sharing.
    </p>
  {/if}
</div>