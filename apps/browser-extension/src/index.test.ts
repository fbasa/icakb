import { describe, expect, it } from "vitest";

import {
  describeBrowserExtensionPackage,
  BROWSER_EXTENSION_PACKAGE_NAME,
  BROWSER_EXTENSION_PACKAGE_VERSION,
} from "./index";

describe("browser extension package", () => {
  it("describes the package scaffold", () => {
    expect(describeBrowserExtensionPackage()).toEqual({
      name: BROWSER_EXTENSION_PACKAGE_NAME,
      version: BROWSER_EXTENSION_PACKAGE_VERSION,
    });
  });
});
