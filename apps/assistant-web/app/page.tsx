import Link from "next/link";

const featureCards = [
  {
    description: "Memory-only sessions, verified identity, and no client-side secrets.",
    title: "Trusted session boundary",
  },
  {
    description: "The assistant talks to the API through a replaceable retrieval adapter.",
    title: "Architecture aligned",
  },
  {
    description: "Structured logs and health surfaces are built in from the start.",
    title: "Operationally visible",
  },
] as const;

const roadmapItems = [
  "Connect the assistant shell to the FastAPI gateway.",
  "Attach session bootstrap and request-correlation headers.",
  "Swap the landing content for the real conversation experience.",
] as const;

export default function Home() {
  return (
    <main className="page-shell">
      <section className="hero">
        <div className="hero-copy">
          <p className="eyebrow">Phase 0 scaffold</p>
          <h1>ICAKB Assistant</h1>
          <p className="lede">
            The standalone assistant app for the secure internal knowledge assistant monorepo. This
            scaffold keeps the rendering surface small, typed, and ready for the API slice.
          </p>
          <div className="hero-actions">
            <Link href="/" className="primary-action">
              App shell
            </Link>
            <span className="secondary-action">Next.js App Router</span>
          </div>
        </div>

        <aside className="status-card" aria-label="Build status summary">
          <p className="status-label">Current milestone</p>
          <p className="status-value">Initial assistant application scaffold</p>
          <p className="status-note">
            Ready to receive the authenticated conversation experience once the gateway lands.
          </p>
        </aside>
      </section>

      <section className="grid" aria-label="Assistant properties">
        {featureCards.map((card) => (
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
          {roadmapItems.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ol>
      </section>
    </main>
  );
}
