<script>
  // No logic — static UI only
</script>

<svelte:head>
  <title>Snip — URL Shortener</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap"
    rel="stylesheet"
  />
</svelte:head>

<main class="root">
  <!-- Atmospheric glow -->
  <div class="glow" aria-hidden="true"></div>

  <!-- Card -->
  <div class="card">

    <!-- Wordmark / title -->
    <div class="card-header">
      <div class="logo-mark" aria-hidden="true">
        <svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M10.5 3H14.25C14.6478 3 15.0294 3.15804 15.3107 3.43934C15.592 3.72064 15.75 4.10218 15.75 4.5V13.5C15.75 13.8978 15.592 14.2794 15.3107 14.5607C15.0294 14.842 14.6478 15 14.25 15H3.75C3.35218 15 2.97064 14.842 2.68934 14.5607C2.40804 14.2794 2.25 13.8978 2.25 13.5V9.75" stroke="#818cf8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M6.75 11.25L15.75 2.25" stroke="#818cf8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M10.5 2.25H15.75V7.5" stroke="#818cf8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      <h1 class="title">URL Shortener</h1>
      <p class="subtitle">Paste a long URL and get a clean, shareable link instantly.</p>
    </div>

    <!-- Form area -->
    <div class="form-body">

      <!-- Input field -->
      <div class="field-group">
        <label class="field-label" for="original-url">Original URL</label>
        <div class="input-wrapper">
          <span class="input-icon" aria-hidden="true">
            <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M8.51194 3.00541C9.18829 2.54366 10.0405 2.37312 10.8561 2.53441C11.6716 2.6957 12.3857 3.17669 12.8232 3.86545C13.2607 4.55421 13.3851 5.39163 13.1695 6.17511C12.9539 6.95859 12.4167 7.61791 11.6925 7.99381L10.5769 8.58988C10.3272 8.72336 10.0398 8.76477 9.76354 8.70775C9.48726 8.65074 9.23896 8.49887 9.06196 8.27902C8.88496 8.05917 8.78987 7.78476 8.79343 7.50294C8.797 7.22113 8.89902 6.94924 9.08147 6.73384L9.74774 5.93188C9.87516 5.77604 9.93625 5.57783 9.91882 5.37877C9.90139 5.17971 9.80672 4.99444 9.65591 4.86334C9.5051 4.73224 9.30955 4.66581 9.10968 4.67807C8.90981 4.69033 8.72371 4.78031 8.58974 4.92887L7.92348 5.73083C7.44828 6.30657 7.22799 7.04907 7.31195 7.78925C7.39591 8.52942 7.77719 9.20573 8.36916 9.67009C8.96113 10.1344 9.71387 10.3479 10.4588 10.2617C11.2037 10.1755 11.8841 9.79639 12.3482 9.20742L13.0145 8.40546" stroke="#475569" stroke-width="1.2" stroke-linecap="round"/>
              <path d="M6.48806 12.0054C5.81171 12.4671 4.95953 12.6377 4.14394 12.4764C3.32836 12.3151 2.61426 11.8341 2.17677 11.1454C1.73928 10.4566 1.6149 9.61919 1.83051 8.83571C2.04612 8.05222 2.58327 7.39291 3.30745 7.01701L4.42313 6.42094C4.67276 6.28746 4.9602 6.24605 5.23648 6.30307C5.51276 6.36008 5.76106 6.51195 5.93806 6.7318C6.11506 6.95165 6.21015 7.22606 6.20659 7.50788C6.20303 7.78969 6.10101 8.06158 5.91856 8.27698L5.25229 9.07894C5.12487 9.23478 5.06378 9.43299 5.08121 9.63205C5.09864 9.83111 5.19331 10.0164 5.34412 10.1475C5.49493 10.2786 5.69048 10.345 5.89035 10.3327C6.09022 10.3205 6.27632 10.2305 6.41029 10.0819L7.07656 9.27995C7.55176 8.70421 7.77205 7.96171 7.68809 7.22153C7.60413 6.48136 7.22285 5.80505 6.63088 5.34069C6.03891 4.87633 5.28617 4.66279 4.54124 4.74901C3.7963 4.83522 3.11594 5.21433 2.65179 5.8033L1.98552 6.60526" stroke="#475569" stroke-width="1.2" stroke-linecap="round"/>
            </svg>
          </span>
          <input
            id="original-url"
            type="url"
            class="input"
            placeholder="https://your-very-long-url.com/goes/here"
            autocomplete="off"
            spellcheck="false"
          />
        </div>
      </div>

      <!-- Primary button -->
      <button class="btn-primary" type="button">
        <span>Shorten URL</span>
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <path d="M2.91669 7H11.0834" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M7.58331 3.5L11.0833 7L7.58331 10.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </button>

      <!-- Divider -->
      <div class="divider" role="separator">
        <span class="divider-line"></span>
        <span class="divider-label">shortened link</span>
        <span class="divider-line"></span>
      </div>

      <!-- Output field -->
      <div class="field-group">
        <label class="field-label" for="short-url">Your Short Link</label>
        <div class="output-row">
          <div class="output-wrapper">
            <span class="output-dot" aria-hidden="true"></span>
            <input
              id="short-url"
              type="text"
              class="output"
              value="https://snip.to/xK9mP2"
              readonly
              tabindex="-1"
            />
          </div>
          <button class="btn-copy" type="button" aria-label="Copy short URL">
            <svg width="15" height="15" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M5 2H10.5C10.7761 2 11 2.22386 11 2.5V10H13.5C13.7761 10 14 10.2239 14 10.5V13.5C14 13.7761 13.7761 14 13.5 14H5.5C5.22386 14 5 13.7761 5 13.5V11H2.5C2.22386 11 2 10.7761 2 10.5V2.5C2 2.22386 2.22386 2 2.5 2H5Z" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
              <path d="M5 2V10.5C5 10.7761 5.22386 11 5.5 11H11V2.5C11 2.22386 10.7761 2 10.5 2H2.5" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <span>Copy</span>
          </button>
        </div>
      </div>

    </div>

    <!-- Card footer hint -->
    <p class="card-footer">Links are active immediately · No account required</p>

  </div>
</main>

<style>
  /* ─── Reset & base ─────────────────────────────────── */
  :global(*, *::before, *::after) {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  :global(html, body) {
    height: 100%;
    font-family: 'Inter', ui-sans-serif, system-ui, -apple-system, sans-serif;
    background-color: #0c0c12;
    color: #e2e8f0;
    -webkit-font-smoothing: antialiased;
  }

  /* ─── Root layout ─────────────────────────────────── */
  .root {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1.5rem;
    position: relative;
    overflow: hidden;
  }

  /* ─── Atmospheric glow ────────────────────────────── */
  .glow {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -60%);
    width: 640px;
    height: 480px;
    background: radial-gradient(
      ellipse at center,
      rgba(99, 102, 241, 0.13) 0%,
      rgba(139, 92, 246, 0.06) 40%,
      transparent 70%
    );
    pointer-events: none;
    z-index: 0;
  }

  /* ─── Card ────────────────────────────────────────── */
  .card {
    position: relative;
    z-index: 1;
    width: 100%;
    max-width: 480px;
    background: #13131c;
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 20px;
    box-shadow:
      0 0 0 1px rgba(99, 102, 241, 0.04),
      0 4px 6px -1px rgba(0, 0, 0, 0.4),
      0 24px 48px -8px rgba(0, 0, 0, 0.5);
    overflow: hidden;
  }

  /* ─── Card header ─────────────────────────────────── */
  .card-header {
    padding: 2.25rem 2.25rem 0;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .logo-mark {
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(99, 102, 241, 0.12);
    border: 1px solid rgba(99, 102, 241, 0.2);
    border-radius: 10px;
    margin-bottom: 0.5rem;
  }

  .title {
    font-size: 1.35rem;
    font-weight: 600;
    letter-spacing: -0.025em;
    color: #f1f5f9;
    line-height: 1.2;
  }

  .subtitle {
    font-size: 0.8125rem;
    font-weight: 400;
    color: #475569;
    line-height: 1.5;
  }

  /* ─── Form body ───────────────────────────────────── */
  .form-body {
    padding: 1.75rem 2.25rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  /* ─── Field group ─────────────────────────────────── */
  .field-group {
    display: flex;
    flex-direction: column;
    gap: 0.375rem;
  }

  .field-label {
    font-size: 0.7rem;
    font-weight: 500;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    color: #475569;
  }

  /* ─── Text input ──────────────────────────────────── */
  .input-wrapper {
    position: relative;
  }

  .input-icon {
    position: absolute;
    left: 0.875rem;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    align-items: center;
    pointer-events: none;
  }

  .input {
    width: 100%;
    padding: 0.6875rem 0.875rem 0.6875rem 2.5rem;
    background: #0f0f18;
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 10px;
    font-family: inherit;
    font-size: 0.8125rem;
    color: #cbd5e1;
    outline: none;
    transition: border-color 0.15s ease, box-shadow 0.15s ease;
    caret-color: #818cf8;
  }

  .input::placeholder {
    color: #2d3748;
  }

  .input:focus {
    border-color: rgba(99, 102, 241, 0.45);
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
  }

  /* ─── Primary button ──────────────────────────────── */
  .btn-primary {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    width: 100%;
    padding: 0.75rem 1.25rem;
    background: linear-gradient(135deg, #6366f1 0%, #7c3aed 100%);
    border: none;
    border-radius: 10px;
    font-family: inherit;
    font-size: 0.875rem;
    font-weight: 500;
    color: #fff;
    cursor: pointer;
    letter-spacing: -0.01em;
    box-shadow:
      0 1px 2px rgba(0, 0, 0, 0.3),
      0 0 0 1px rgba(99, 102, 241, 0.3),
      inset 0 1px 0 rgba(255, 255, 255, 0.1);
    transition: opacity 0.15s ease, transform 0.1s ease;
    margin-top: 0.125rem;
  }

  .btn-primary:hover {
    opacity: 0.9;
  }

  .btn-primary:active {
    transform: scale(0.99);
  }

  /* ─── Divider ─────────────────────────────────────── */
  .divider {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin: 0.25rem 0;
  }

  .divider-line {
    flex: 1;
    height: 1px;
    background: rgba(255, 255, 255, 0.05);
  }

  .divider-label {
    font-size: 0.6875rem;
    font-weight: 400;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #334155;
    white-space: nowrap;
  }

  /* ─── Output row ──────────────────────────────────── */
  .output-row {
    display: flex;
    gap: 0.5rem;
    align-items: stretch;
  }

  .output-wrapper {
    flex: 1;
    position: relative;
    min-width: 0;
  }

  .output-dot {
    position: absolute;
    left: 0.875rem;
    top: 50%;
    transform: translateY(-50%);
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #6366f1;
    box-shadow: 0 0 6px rgba(99, 102, 241, 0.7);
  }

  .output {
    width: 100%;
    padding: 0.6875rem 0.875rem 0.6875rem 2.25rem;
    background: rgba(99, 102, 241, 0.06);
    border: 1px solid rgba(99, 102, 241, 0.18);
    border-radius: 10px;
    font-family: 'Inter', ui-monospace, monospace;
    font-size: 0.8125rem;
    font-weight: 400;
    color: #a5b4fc;
    outline: none;
    cursor: default;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    letter-spacing: 0.01em;
  }

  /* ─── Copy button ─────────────────────────────────── */
  .btn-copy {
    flex-shrink: 0;
    display: flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.6875rem 0.9rem;
    background: #1a1a26;
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 10px;
    font-family: inherit;
    font-size: 0.8rem;
    font-weight: 500;
    color: #94a3b8;
    cursor: pointer;
    white-space: nowrap;
    transition: background 0.15s ease, color 0.15s ease, border-color 0.15s ease;
  }

  .btn-copy:hover {
    background: #1e1e30;
    border-color: rgba(99, 102, 241, 0.3);
    color: #c7d2fe;
  }

  .btn-copy:active {
    transform: scale(0.98);
  }

  /* ─── Card footer ─────────────────────────────────── */
  .card-footer {
    padding: 0.875rem 2.25rem 1.5rem;
    font-size: 0.7rem;
    color: #1e293b;
    text-align: center;
    letter-spacing: 0.02em;
    border-top: 1px solid rgba(255, 255, 255, 0.04);
  }

  /* ─── Responsive ──────────────────────────────────── */
  @media (max-width: 520px) {
    .root {
      padding: 1rem;
      align-items: flex-start;
      padding-top: 3rem;
    }

    .card {
      border-radius: 16px;
    }

    .card-header {
      padding: 1.75rem 1.5rem 0;
    }

    .form-body {
      padding: 1.5rem;
    }

    .card-footer {
      padding: 0.875rem 1.5rem 1.25rem;
    }
  }
</style>
