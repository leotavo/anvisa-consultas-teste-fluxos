import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  timeout: 30000,
  retries: 1,
  reporter: [['html', { outputFolder: 'reports' }]],
  projects: [
    {
      name: 'Chromium',
      use: {
        ...devices['Desktop Chrome'],
        headless: false,
      },
    },
    {
      name: 'Firefox',
      use: {
        ...devices['Desktop Firefox'],
        headless: false,
      },
    },
    {
      name: 'WebKit',
      use: {
        ...devices['Desktop Safari'],
        headless: false,
      },
    },
  ],
  use: {
    viewport: { width: 1280, height: 720 },
    actionTimeout: 0,
    ignoreHTTPSErrors: true,
  },
});