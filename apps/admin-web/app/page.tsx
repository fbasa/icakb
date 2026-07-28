import Link from "next/link";

const overviewCards = [
  {
    description: "Scoped administrative actions stay server-side and use verified identity.",
    title: "Controlled access",
  },
  {
    description: "Operational views focus on tenants, sync status, and deployment health.",
    title: "Operational clarity",
  },
  {
    description: "The shell is intentionally thin so shared packages can evolve independently.",
    title: "Boundary aligned",
  },
] as const;

const workItems = [
  "Connect authenticated admin routes to the backend policy context.",
  "Expose tenant, sync, and release controls through validated APIs.",
  "Replace this scaffold with the production operations workspace.",
] as const;

export default function Home() {
  return (
    <main className="page-shell">
      <section className="hero">
        <div className="hero-copy">
          <p className="eyebrow">Phase 0 scaffold</p>
          <h1>ICAKB Admin</h1>
          <p className="lede">
            The standalone administration app for the ICAKB monorepo. This scaffold keeps the admin
            surface separate from the assistant UI and ready for policy-gated workflows.
          </p>
          <div className="hero-actions">
            <Link href="/" className="primary-action">
              Admin shell
            </Link>
            <span className="secondary-action">Next.js App Router</span>
          </div>
        </div>

        <aside className="status-card" aria-label="Build status summary">
          <p className="status-label">Current milestone</p>
          <p className="status-value">Initial administration application scaffold</p>
          <p className="status-note">
            Ready for tenant operations, release controls, and audit-friendly admin workflows.
          </p>
        </aside>
      </section>

      <section className="grid" aria-label="Administration properties">
        {overviewCards.map((card) => (
          <article key={card.title} className="feature-card">
            <h2>{card.title}</h2>
            <p>{card.description}</p>
          </article>
        ))}
      </section>

      <section className="roadmap" aria-label="Next steps">
        <div>
          <p className="eyebrow">Next steps</p>
          <h2>What this scaffold prepares for</h2>
        </div>
        <ol>
          {workItems.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ol>
      </section>
    </main>
  );
}
