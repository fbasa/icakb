import { describe, expect, it } from "vitest";

import {
  describeWidgetLoaderPackage,
  WIDGET_LOADER_PACKAGE_NAME,
  WIDGET_LOADER_PACKAGE_VERSION,
} from "./index";

describe("widget loader package", () => {
  it("describes the package scaffold", () => {
    expect(describeWidgetLoaderPackage()).toEqual({
      name: WIDGET_LOADER_PACKAGE_NAME,
      version: WIDGET_LOADER_PACKAGE_VERSION,
    });
  });
});
