import type { PropsWithChildren } from "react";

import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

vi.mock("next/link", () => ({
  default: ({
    children,
    className,
    href,
  }: PropsWithChildren<{ className?: string; href: string }>) => (
    <a className={className} href={href}>
      {children}
    </a>
  ),
}));

import Home from "./page";

describe("admin home page", () => {
  it("renders the scaffold hero", () => {
    render(<Home />);

    expect(screen.getByRole("heading", { name: "ICAKB Admin" })).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "Admin shell" })).toHaveAttribute("href", "/");
    expect(screen.getByText("Initial administration application scaffold")).toBeInTheDocument();
  });
});
