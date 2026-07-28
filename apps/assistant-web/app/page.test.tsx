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

describe("assistant home page", () => {
  it("renders the scaffold hero", () => {
    render(<Home />);

    expect(screen.getByRole("heading", { name: "ICAKB Assistant" })).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "App shell" })).toHaveAttribute("href", "/");
    expect(screen.getByText("Initial assistant application scaffold")).toBeInTheDocument();
  });
});
