export const BROWSER_EXTENSION_PACKAGE_NAME = "@icakb/browser-extension" as const;
export const BROWSER_EXTENSION_PACKAGE_VERSION = "0.0.0" as const;

export type BrowserExtensionPackageDescriptor = Readonly<{
  name: typeof BROWSER_EXTENSION_PACKAGE_NAME;
  version: typeof BROWSER_EXTENSION_PACKAGE_VERSION;
}>;

export function describeBrowserExtensionPackage(): BrowserExtensionPackageDescriptor {
  return {
    name: BROWSER_EXTENSION_PACKAGE_NAME,
    version: BROWSER_EXTENSION_PACKAGE_VERSION,
  };
}
