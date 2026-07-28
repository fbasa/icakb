import { expect, test } from "@playwright/test";

test("assistant scaffold renders the landing page", async ({ page }) => {
  await page.goto("/");

  await expect(page.getByRole("heading", { name: "ICAKB Assistant" })).toBeVisible();
  await expect(page.getByRole("link", { name: "App shell" })).toHaveAttribute("href", "/");
  await expect(page.getByText("Initial assistant application scaffold")).toBeVisible();
});
