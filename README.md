# ReconX 🔎  
### A recon framework built while hunting bugs

ReconX is my personal reconnaissance setup that grew out of real bug bounty work.  
It’s not meant to be loud, fast, or “all-in-one”.

It exists to:
- reduce repetitive recon work
- keep results readable
- leave room for manual testing (where bugs actually come from)

---

## What this tool is (and isn’t)

**ReconX is:**
- a wrapper around proven recon tools
- focused on coverage, not speed
- built to support manual hacking

**ReconX is NOT:**
- a magic bug finder
- a one-click bounty machine
- a replacement for reading JavaScript or understanding logic

If you just want automated findings, this probably isn’t for you.

---

## Why I built this

I kept running into the same problem:
- tons of output
- too much noise
- not enough time spent understanding what I found

So I built ReconX to slow things down:
- group results per target
- highlight interesting surfaces
- make JavaScript recon easier

The goal is simple:  
**less scanning, more thinking.**

---

## What ReconX does during recon

- collects subdomains from multiple sources
- checks what’s actually alive
- looks for open ports worth attention
- pulls URLs from current and historical data
- parses JavaScript for hidden paths and parameters
- runs nuclei carefully (only where it makes sense)

Everything is saved as plain text so you can grep, filter, and test manually.
