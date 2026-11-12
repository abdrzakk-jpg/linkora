


<script>
  // ── State ────────────────────────────────────────────────
  let inputUrl = "";
  let shortUrl = "";
  let urlValid = null; // true | false | null
  let loading = false;
  let copied = false;
  let copyTimer = null;

  // error: null | { kind: '422'|'500'|'network', message: string }
  let error = null;

  // ── Derived ──────────────────────────────────────────────
  $: hasResult = shortUrl !== "";
  $: canSubmit = inputUrl.trim() !== "" && !loading;

  // ── API call ─────────────────────────────────────────────
  async function shorten() {
    if (!canSubmit) return;

    loading = true;
    error = null;
    shortUrl = "";
    urlValid = null;

    try {
      const res = await fetch("http://localhost:8000/v1/sh", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: inputUrl.trim() }),
      });

      if (res.status === 201) {
        const data = await res.json();
        shortUrl = data.url;
        urlValid = data.valid;
        error = null;
      } else if (res.status === 422) {
        const data = await res.json();
        // Pydantic v2 detail is an array of objects
        const first = data?.detail?.[0];
        const msg =
          first?.msg ?? "Enter a valid URL (e.g. https://example.com).";
        error = { kind: "422", message: msg };
      } else if (res.status === 500) {
        error = {
          kind: "500",
          message: "Server error. Try again in a moment.",
        };
      } else {
        error = {
          kind: "500",
          message: `Unexpected response (${res.status}).`,
        };
      }
    } catch {
      error = {
        kind: "network",
        message: "Could not reach the server. Check your connection.",
      };
    } finally {
      loading = false;
    }
  }

  // ── Copy ─────────────────────────────────────────────────
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
  // ── Visit ─────────────────────────────────────────────────
  async function visit(url) {
    document.location.href=url
  }

  // ── Enter key ────────────────────────────────────────────
  function onKeydown(e) {
    if (e.key === "Enter") shorten();
  }

  // ── Theme ────────────────────────────────────────────────
  let dark = true;
  function toggleTheme() {
    dark = !dark;
    if (typeof document !== "undefined") {
      document.documentElement.classList.toggle("dark", dark);
    }
  }
</script>

<svelte:head>
  <title>Linkora</title>
  <meta name="description" content="Shorten any URL instantly." />
</svelte:head>

<div class="root" class:dark>
  <div class="page">
    <!-- ── Theme toggle ── -->
    <button
      class="theme-btn"
      on:click={toggleTheme}
      aria-label={dark ? "Switch to light mode" : "Switch to dark mode"}
      type="button"
    >
      {#if dark}
        <!-- Sun icon -->
        <svg
          width="15"
          height="15"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
        >
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
        <!-- Moon icon -->
        <svg
          width="15"
          height="15"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
        >
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z" />
        </svg>
      {/if}
    </button>

    <!-- ── Card ── -->
    <article class="card">
      <!-- Header -->
      <header class="card-head">
        <div class="wordmark">
          <!-- Link/shortcut icon -->
          <svg
            class="wm-icon"
            width="20"
            height="20"
            viewBox="0 0 20 20"
            fill="none"
            aria-hidden="true"
          >
            <path
              d="M11.5 4.5H15.5C15.7761 4.5 16 4.72386 16 5V15C16 15.2761 15.7761 15.5 15.5 15.5H4.5C4.22386 15.5 4 15.2761 4 15V11"
              stroke="currentColor"
              stroke-width="1.5"
              stroke-linecap="round"
            />
            <path
              d="M8.5 11.5L15.5 4.5"
              stroke="currentColor"
              stroke-width="1.5"
              stroke-linecap="round"
            />
            <path
              d="M11.5 4.5H15.5V8.5"
              stroke="currentColor"
              stroke-width="1.5"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </svg>
          <span class="wm-text">Linkora</span>
        </div>
        <p class="card-sub">Paste a URL. Get a link that fits.</p>
      </header>

      <!-- Body -->
      <div class="card-body">
        <!-- Input field -->
        <div class="field">
          <label class="field-label" for="url-input">URL to shorten</label>
          <input
            id="url-input"
            class="input"
            class:input-err={error}
            type="url"
            placeholder="https://example.com/very/long/path"
            bind:value={inputUrl}
            on:keydown={onKeydown}
            disabled={loading}
            autocomplete="off"
            spellcheck="false"
          />
        </div>

        <!-- Inline error -->
        {#if error}
          <div class="err-row" role="alert">
            <svg
              width="13"
              height="13"
              viewBox="0 0 16 16"
              fill="none"
              aria-hidden="true"
              style="flex-shrink:0;margin-top:1px"
            >
              <circle
                cx="8"
                cy="8"
                r="7"
                stroke="currentColor"
                stroke-width="1.5"
              />
              <line
                x1="8"
                y1="5"
                x2="8"
                y2="8.5"
                stroke="currentColor"
                stroke-width="1.6"
                stroke-linecap="round"
              />
              <circle cx="8" cy="11" r="0.8" fill="currentColor" />
            </svg>
            <span>{error.message}</span>
          </div>
        {/if}

        <!-- Submit -->
        <button
          class="btn-primary"
          type="button"
          on:click={shorten}
          disabled={!canSubmit}
          aria-busy={loading}
        >
          {#if loading}
            <span class="spinner" aria-hidden="true"></span>
            Shortening…
          {:else}
            Shorten URL
          {/if}
        </button>

        <!-- Output -->
        {#if hasResult}
          <div class="result" aria-live="polite">
            <!-- Validity row -->
            <div class="validity-row">
              <span class="validity-label">Original URL</span>
              {#if urlValid === true}
                <span class="badge badge-ok">
                  <span class="dot"></span>Reachable
                </span>
              {:else if urlValid === false}
                <span class="badge badge-warn">
                  <span class="dot"></span>Unreachable
                </span>
              {/if}
            </div>

            <!-- Short URL field -->
            <div class="field">
              <label class="field-label" for="short-out">Short link</label>
              <div class="out-row">
                <input
                  id="short-out"
                  class="input out-input"
                  type="text"
                  value={shortUrl}
                  readonly
                  tabindex="-1"
                />
                <button
                  class="btn-copy"
                  class:btn-copied={copied}
                  type="button"
                  on:click={copy}
                  aria-label={copied ? "Copied!" : "Copy link"}
                >
                  {#if copied}
                    <!-- Checkmark -->
                    <svg
                      width="14"
                      height="14"
                      viewBox="0 0 16 16"
                      fill="none"
                      aria-hidden="true"
                    >
                      <polyline
                        points="2.5,8.5 6.5,12.5 13.5,4.5"
                        stroke="currentColor"
                        stroke-width="1.7"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                      />
                    </svg>
                    Copied
                  {:else}
                    <!-- Copy pages -->
                    <svg
                      width="14"
                      height="14"
                      viewBox="0 0 16 16"
                      fill="none"
                      aria-hidden="true"
                    >
                      <rect
                        x="5.5"
                        y="5.5"
                        width="8"
                        height="8"
                        rx="1"
                        stroke="currentColor"
                        stroke-width="1.4"
                      />
                      <path
                        d="M3.5 10.5V3.5C3.5 2.94772 3.94772 2.5 4.5 2.5H11.5"
                        stroke="currentColor"
                        stroke-width="1.4"
                        stroke-linecap="round"
                      />
                    </svg>
                    Copy
                  {/if}
                </button>

                <!-- Go-to Button -->
                <button class="btn-copy" type="button" on:click={()=>visit(shortUrl.trim())}>
                  <!-- visit page -->
                  <svg
                    width="14"
                    height="14"
                    viewBox="0 0 16 16"
                    fill="none"
                    aria-hidden="true"
                  >
                    <path
                      d="M3 8H13M8.5 3.5L13 8L8.5 12.5"
                      stroke="currentColor"
                      stroke-width="1.4"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                    />
                  </svg>
                  visit
                </button>
              </div>
            </div>

            <!-- Unreachable warning -->
            {#if urlValid === false}
              <p class="warn-note">
                Link created — but the original URL appears unreachable.
                Double-check the address before sharing.
              </p>
            {/if}
          </div>
        {/if}
      </div>
      <!-- /card-body -->
    </article>
  </div>
</div>

<style>
  /* ── Design tokens ───────────────────────────────────── */
  :global(:root) {
    /* Surfaces — light */
    --bg: #f5f5f7;
    --card: #ffffff;
    --input-bg: #ffffff;
    --input-bg-out: #fafafc;
    /* Ink */
    --ink: #1d1d1f;
    --ink-2: #3a3a3c;
    --ink-3: #6e6e73;
    --ink-4: #aeaeb2;
    /* Borders */
    --border: #d2d2d7;
    --border-soft: #e8e8ed;
    /* Accent — Indigo (brief spec) */
    --accent: #5856d6;
    --accent-h: #3634c7;
    --accent-dim: rgba(88, 86, 214, 0.12);
    --accent-fg: #ffffff;
    /* Semantic */
    --ok: #34c759;
    --ok-bg: #f0fff4;
    --ok-border: rgba(52, 199, 89, 0.25);
    --warn: #f59e0b;
    --warn-bg: #fffbeb;
    --warn-border: rgba(245, 158, 11, 0.25);
    --err: #ff3b30;
    --err-bg: #fff5f5;
    --err-border: rgba(255, 59, 48, 0.25);
    /* Shadow */
    --shadow: 0 1px 2px rgba(0, 0, 0, 0.04), 0 4px 20px rgba(0, 0, 0, 0.07);
    /* Type */
    --f-display: "SF Pro Display", ui-sans-serif, system-ui, -apple-system,
      sans-serif;
    --f-body: "SF Pro Text", ui-sans-serif, system-ui, -apple-system, sans-serif;
  }

  :global(.dark) {
    --bg: #000000;
    --card: #1c1c1e;
    --input-bg: #2c2c2e;
    --input-bg-out: #252527;
    --ink: #f5f5f7;
    --ink-2: #ebebf0;
    --ink-3: #aeaeb2;
    --ink-4: #636366;
    --border: #38383a;
    --border-soft: #2c2c2e;
    --accent: #7d7aff;
    --accent-h: #9d9bff;
    --accent-dim: rgba(125, 122, 255, 0.15);
    --accent-fg: #ffffff;
    --ok: #30d158;
    --ok-bg: rgba(48, 209, 88, 0.1);
    --ok-border: rgba(48, 209, 88, 0.2);
    --warn: #ffd60a;
    --warn-bg: rgba(255, 214, 10, 0.08);
    --warn-border: rgba(255, 214, 10, 0.2);
    --err: #ff453a;
    --err-bg: rgba(255, 69, 58, 0.1);
    --err-border: rgba(255, 69, 58, 0.2);
    --shadow: 0 1px 3px rgba(0, 0, 0, 0.5), 0 8px 32px rgba(0, 0, 0, 0.45);
  }

  /* ── Reset ───────────────────────────────────────────── */
  :global(*, *::before, *::after) {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  :global(html, body) {
    height: 100%;
  }
  :global(body) {
    font-family: var(--f-body);
    -webkit-font-smoothing: antialiased;
  }

  /* ── Root ────────────────────────────────────────────── */
  .root {
    min-height: 100vh;
    background: var(--bg);
    color: var(--ink);
    transition:
      background 0.18s,
      color 0.18s;
  }

  .page {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 2rem 1rem;
    position: relative;
  }

  /* ── Theme toggle ────────────────────────────────────── */
  .theme-btn {
    position: fixed;
    top: 1.125rem;
    right: 1.125rem;
    width: 34px;
    height: 34px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 0; /* sharp per brief */
    color: var(--ink-3);
    cursor: pointer;
    z-index: 50;
    transition:
      color 0.12s,
      background 0.12s;
  }
  .theme-btn:hover {
    color: var(--ink);
  }
  .theme-btn:active {
    transform: scale(0.94);
  }

  /* ── Card ────────────────────────────────────────────── */
  .card {
    width: 100%;
    max-width: 476px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 0; /* sharp corners — brief spec */
    box-shadow: var(--shadow);
  }

  /* ── Card header ─────────────────────────────────────── */
  .card-head {
    padding: 1.875rem 2rem 1.5rem;
    border-bottom: 1px solid var(--border-soft);
  }

  .wordmark {
    display: flex;
    align-items: center;
    gap: 0.45rem;
    margin-bottom: 0.45rem;
  }

  .wm-icon {
    color: var(--accent);
    flex-shrink: 0;
  }

  .wm-text {
    font-family: var(--f-display);
    font-size: 1.3125rem; /* 21px — DESIGN.md tagline scale */
    font-weight: 600;
    letter-spacing: -0.022em; /* DESIGN.md: negative tracking on display */
    color: var(--ink);
    line-height: 1;
  }

  .card-sub {
    font-family: var(--f-body);
    font-size: 0.875rem; /* 14px — DESIGN.md caption */
    font-weight: 400;
    letter-spacing: -0.014em;
    line-height: 1.43;
    color: var(--ink-3);
  }

  /* ── Card body ───────────────────────────────────────── */
  .card-body {
    padding: 1.625rem 2rem 2rem;
    display: flex;
    flex-direction: column;
    gap: 0.875rem;
  }

  /* ── Field ───────────────────────────────────────────── */
  .field {
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
  }

  .field-label {
    font-size: 0.75rem; /* 12px fine-print */
    font-weight: 400;
    letter-spacing: -0.008em;
    color: var(--ink-4);
    line-height: 1;
    user-select: none;
  }

  /* ── Input ───────────────────────────────────────────── */
  .input {
    width: 100%;
    height: 44px; /* DESIGN.md: 44px touch min */
    padding: 0 0.875rem;
    background: var(--input-bg);
    border: 1px solid var(--border);
    border-radius: 0; /* sharp */
    font-family: var(--f-body);
    font-size: 0.9375rem; /* 15px — between caption & body */
    font-weight: 400;
    letter-spacing: -0.02em;
    color: var(--ink);
    outline: none;
    caret-color: var(--accent);
    transition:
      border-color 0.1s,
      box-shadow 0.1s,
      background 0.15s;
  }
  .input::placeholder {
    color: var(--ink-4);
  }
  .input:focus {
    border-color: var(--accent);
    box-shadow: 0 0 0 2.5px var(--accent-dim);
  }
  .input:disabled {
    opacity: 0.45;
    cursor: not-allowed;
  }
  .input-err {
    border-color: var(--err) !important;
  }
  .input-err:focus {
    box-shadow: 0 0 0 2.5px rgba(255, 59, 48, 0.14) !important;
  }

  /* ── Error row ───────────────────────────────────────── */
  .err-row {
    display: flex;
    align-items: flex-start;
    gap: 0.45rem;
    padding: 0.625rem 0.75rem;
    background: var(--err-bg);
    border: 1px solid var(--err-border);
    border-radius: 0;
    font-size: 0.8125rem;
    font-weight: 400;
    line-height: 1.45;
    color: var(--err);
  }

  /* ── Primary button ──────────────────────────────────── */
  .btn-primary {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.45rem;
    width: 100%;
    height: 44px;
    padding: 0 1.25rem;
    background: var(--accent);
    border: 1px solid transparent;
    border-radius: 0;
    font-family: var(--f-body);
    font-size: 0.9375rem;
    font-weight: 400;
    letter-spacing: -0.02em;
    color: var(--accent-fg);
    cursor: pointer;
    transition:
      background 0.1s,
      opacity 0.1s,
      transform 0.07s;
  }
  .btn-primary:hover:not(:disabled) {
    background: var(--accent-h);
  }
  .btn-primary:active:not(:disabled) {
    transform: scale(0.97);
  } /* DESIGN.md: scale(0.95) on press */
  .btn-primary:disabled {
    opacity: 0.38;
    cursor: not-allowed;
  }

  /* ── Spinner ─────────────────────────────────────────── */
  .spinner {
    width: 13px;
    height: 13px;
    border: 1.75px solid rgba(255, 255, 255, 0.3);
    border-top-color: #fff;
    border-radius: 50%;
    animation: spin 0.6s linear infinite;
    flex-shrink: 0;
  }
  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }
  @media (prefers-reduced-motion: reduce) {
    .spinner {
      animation: none;
      opacity: 0.6;
    }
  }

  /* ── Result block ────────────────────────────────────── */
  .result {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    padding-top: 0.625rem;
    border-top: 1px solid var(--border-soft);
  }

  /* ── Validity row ────────────────────────────────────── */
  .validity-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.5rem;
  }

  .validity-label {
    font-size: 0.75rem;
    font-weight: 400;
    letter-spacing: -0.008em;
    color: var(--ink-4);
  }

  /* ── Badge ───────────────────────────────────────────── */
  .badge {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.6875rem; /* 11px — micro */
    font-weight: 600;
    letter-spacing: 0.01em;
    padding: 0.2rem 0.5rem;
    border-radius: 2px; /* minimal radius — not pill */
    line-height: 1.5;
    border: 1px solid transparent;
  }

  .dot {
    width: 5px;
    height: 5px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .badge-ok {
    background: var(--ok-bg);
    color: var(--ok);
    border-color: var(--ok-border);
  }
  .badge-ok .dot {
    background: var(--ok);
  }
  .badge-warn {
    background: var(--warn-bg);
    color: var(--warn);
    border-color: var(--warn-border);
  }
  .badge-warn .dot {
    background: var(--warn);
  }

  /* ── Output row ──────────────────────────────────────── */
  .out-row {
    display: flex;
    gap: 0.375rem;
  }

  .out-input {
    flex: 1;
    min-width: 0;
    background: var(--input-bg-out);
    border-color: var(--border-soft);
    color: var(--accent);
    font-size: 0.875rem;
    cursor: default;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .out-input:focus {
    border-color: var(--border);
    box-shadow: none;
  }

  /* ── Copy button ─────────────────────────────────────── */
  .btn-copy {
    flex-shrink: 0;
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    height: 44px;
    padding: 0 0.875rem;
    background: var(--input-bg);
    border: 1px solid var(--border);
    border-radius: 0;
    font-family: var(--f-body);
    font-size: 0.8125rem;
    font-weight: 400;
    letter-spacing: -0.012em;
    color: var(--ink-3);
    cursor: pointer;
    white-space: nowrap;
    transition:
      background 0.1s,
      color 0.1s,
      border-color 0.1s,
      transform 0.07s;
  }
  .btn-copy:hover {
    background: var(--border-soft);
    color: var(--ink);
  }
  .btn-copy:active {
    transform: scale(0.95);
  }

  .btn-copied {
    background: var(--ok-bg) !important;
    border-color: var(--ok-border) !important;
    color: var(--ok) !important;
  }

  /* ── Warn note ───────────────────────────────────────── */
  .warn-note {
    font-size: 0.8125rem;
    font-weight: 400;
    line-height: 1.5;
    letter-spacing: -0.01em;
    color: var(--warn);
    background: var(--warn-bg);
    border: 1px solid var(--warn-border);
    border-radius: 0;
    padding: 0.625rem 0.75rem;
  }

  /* ── Responsive ──────────────────────────────────────── */
  @media (max-width: 520px) {
    .page {
      padding: 1rem 0.75rem;
      align-items: flex-start;
      padding-top: 3.5rem;
    }
    .card-head {
      padding: 1.5rem 1.25rem 1.25rem;
    }
    .card-body {
      padding: 1.25rem 1.25rem 1.5rem;
    }
    .theme-btn {
      top: 0.75rem;
      right: 0.75rem;
    }
  }
</style>
