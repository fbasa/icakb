import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";

export default defineConfig([
  ...nextVitals,
  {
    settings: {
      next: {
        rootDir: ["apps/admin-web", "apps/assistant-web"],
      },
    },
  },
  globalIgnores([
    "**/.next/**",
    "**/out/**",
    "**/build/**",
    "**/coverage/**",
    "**/dist/**",
    "**/next-env.d.ts",
  ]),
]);
