export const WIDGET_LOADER_PACKAGE_NAME = "@icakb/widget-loader" as const;
export const WIDGET_LOADER_PACKAGE_VERSION = "0.0.0" as const;

export type WidgetLoaderPackageDescriptor = Readonly<{
  name: typeof WIDGET_LOADER_PACKAGE_NAME;
  version: typeof WIDGET_LOADER_PACKAGE_VERSION;
}>;

export function describeWidgetLoaderPackage(): WidgetLoaderPackageDescriptor {
  return {
    name: WIDGET_LOADER_PACKAGE_NAME,
    version: WIDGET_LOADER_PACKAGE_VERSION,
  };
}
