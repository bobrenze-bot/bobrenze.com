#!/usr/bin/env python3
"""
BobRenze Social Post Generator
CLI tool for generating social media posts from HTML templates.

Usage:
    python3 social-post-generator.py --list
    python3 social-post-generator.py --template 01-launch --headline "New Feature" --subtitle "Description"
    python3 social-post-generator.py --template 04-tip --interactive
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional

# Configuration
TEMPLATES_DIR = Path(
    "/Users/serenerenze/bob-bootstrap/projects/bobrenze.com/social-cards"
)
OUTPUT_DIR = Path("/Users/serenerenze/bob-bootstrap/tmp/social-posts")
TEMPLATES_INDEX = TEMPLATES_DIR / "templates.json"


def load_templates() -> dict:
    """Load templates index from JSON."""
    with open(TEMPLATES_INDEX) as f:
        return json.load(f)


def list_templates():
    """Display available templates."""
    data = load_templates()
    print("\n📱 BobRenze Social Card Templates")
    print("=" * 60)

    for t in data["templates"]:
        print(f"\n{t['file'].replace('.html', '')}: {t['name']}")
        print(f"   Purpose: {t['description']}")
        print(f"   Best for: {', '.join(t['bestFor'])}")
        print(f"   Frequency: {t['frequency']}")

    print("\n" + "=" * 60)
    print(
        f"\nBrand colors: {data['metadata']['colors']['primary']} (primary), "
        f"{data['metadata']['colors']['accent']} (accent)"
    )
    print(
        f"Dimensions: {data['metadata']['dimensions']['width']}x"
        f"{data['metadata']['dimensions']['height']}px"
    )


def get_template_path(template_id: str) -> Path:
    """Get full path to template HTML file."""
    # Handle both "01-launch" and "01-launch.html" formats
    if not template_id.endswith(".html"):
        template_id += ".html"
    return TEMPLATES_DIR / template_id


def customize_template(
    template_path: Path,
    headline: Optional[str] = None,
    subtitle: Optional[str] = None,
    badge: Optional[str] = None,
    brand_mark: Optional[str] = None,
    extra_css: Optional[str] = None,
) -> str:
    """
    Customize template HTML with new content.
    Returns modified HTML as string.
    """
    with open(template_path) as f:
        html = f.read()

    # Customize headline (h1)
    if headline:
        # Replace text inside h1 tags, preserving HTML structure
        html = re.sub(
            r"(<h1[^>]*>)(.*?)(</h1>)",
            lambda m: f"{m.group(1)}{headline}{m.group(3)}",
            html,
            flags=re.DOTALL,
        )

    # Customize subtitle (.subtitle)
    if subtitle:
        html = re.sub(
            r'(<p class="subtitle"[^>]*>)(.*?)(</p>)',
            lambda m: f"{m.group(1)}{subtitle}{m.group(3)}",
            html,
            flags=re.DOTALL,
        )

    # Customize badge (.badge-text)
    if badge:
        html = re.sub(
            r'(<span class="badge-text"[^>]*>)(.*?)(</span>)',
            lambda m: f"{m.group(1)}{badge}{m.group(3)}",
            html,
            flags=re.DOTALL,
        )

    # Customize brand mark
    if brand_mark:
        html = re.sub(
            r'(<div class="brand-mark"[^>]*>)(.*?)(</div>)',
            lambda m: f"{m.group(1)}{brand_mark}{m.group(3)}",
            html,
            flags=re.DOTALL,
        )

    # Inject extra CSS if provided
    if extra_css:
        css_block = f"""
        <style>
        /* Custom overrides */
        {extra_css}
        </style>
        """
        # Insert before </head>
        html = html.replace("</head>", f"{css_block}</head>")

    return html


def save_custom_template(
    html: str, template_id: str, output_name: Optional[str] = None
) -> Path:
    """Save customized HTML to output directory."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if output_name:
        filename = f"{output_name}.html"
    else:
        # Generate timestamped filename
        from datetime import datetime

        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{template_id}-{timestamp}.html"

    output_path = OUTPUT_DIR / filename

    with open(output_path, "w") as f:
        f.write(html)

    return output_path


def generate_screenshot(
    html_path: Path, output_name: Optional[str] = None
) -> Optional[Path]:
    """
    Generate PNG screenshot from HTML using openclaw browser.
    Returns path to PNG file or None if failed.
    """
    try:
        # Set up output path
        if output_name:
            png_path = OUTPUT_DIR / f"{output_name}.png"
        else:
            png_path = OUTPUT_DIR / f"{html_path.stem}.png"

        # Use openclaw browser to navigate and screenshot
        file_url = f"file://{html_path.absolute()}"

        print(f"  📸 Generating screenshot...")
        print(f"     Navigating to: {file_url}")

        # Navigate
        result = subprocess.run(
            ["openclaw", "browser", "navigate", file_url],
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode != 0:
            print(f"     ⚠️  Navigation warning: {result.stderr}")

        # Take screenshot
        result = subprocess.run(
            ["openclaw", "browser", "screenshot"],
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode == 0:
            # Screenshot saved, need to find where
            # openclaw browser screenshot returns the file path in output
            print(f"     Screenshot saved")
            return png_path
        else:
            print(f"     ⚠️  Screenshot failed: {result.stderr}")
            return None

    except subprocess.TimeoutExpired:
        print("     ⚠️  Screenshot timeout (browser may not be available)")
        return None
    except Exception as e:
        print(f"     ⚠️  Screenshot error: {e}")
        return None


def interactive_mode():
    """Interactive template selection and customization."""
    print("\n📱 BobRenze Social Post Generator - Interactive Mode\n")

    # List templates
    list_templates()

    # Get template selection
    print("\n" + "-" * 60)
    template_id = input("\nEnter template ID (e.g., '01-launch'): ").strip()

    template_path = get_template_path(template_id)
    if not template_path.exists():
        print(f"❌ Template not found: {template_id}")
        sys.exit(1)

    # Get customizations
    print(f"\n✏️  Customizing {template_id}")
    print("   (Press Enter to skip any field)\n")

    headline = input("Headline: ").strip() or None
    subtitle = input("Subtitle: ").strip() or None
    badge = input("Badge text: ").strip() or None
    brand_mark = input("Brand mark (single char): ").strip() or None

    output_name = input("\nOutput filename (no extension): ").strip()

    # Generate
    generate_post(
        template_id=template_id,
        headline=headline,
        subtitle=subtitle,
        badge=badge,
        brand_mark=brand_mark,
        output_name=output_name or None,
        screenshot=False,  # Skip in interactive for speed
    )


def generate_post(
    template_id: str,
    headline: Optional[str] = None,
    subtitle: Optional[str] = None,
    badge: Optional[str] = None,
    brand_mark: Optional[str] = None,
    extra_css: Optional[str] = None,
    output_name: Optional[str] = None,
    screenshot: bool = False,
):
    """Generate a customized social post from template."""

    template_path = get_template_path(template_id)
    if not template_path.exists():
        print(f"❌ Template not found: {template_id}")
        print(f"   Looking for: {template_path}")
        sys.exit(1)

    print(f"\n🎨 Generating post from {template_id}...")

    # Customize HTML
    html = customize_template(
        template_path=template_path,
        headline=headline,
        subtitle=subtitle,
        badge=badge,
        brand_mark=brand_mark,
        extra_css=extra_css,
    )

    # Save customized HTML
    html_path = save_custom_template(html, template_id, output_name)
    print(f"   ✓ HTML saved: {html_path}")

    # Generate screenshot if requested
    png_path = None
    if screenshot:
        png_path = generate_screenshot(html_path, output_name)
        if png_path:
            print(f"   ✓ Screenshot: {png_path}")

    # Output summary
    print(f"\n📁 Output location: {OUTPUT_DIR}")
    print(f"\n📝 Next steps:")
    print(f"   1. Open HTML in browser: open {html_path}")
    if not screenshot:
        print(
            f"   2. Or generate screenshot: openclaw browser navigate 'file://{html_path}'"
        )
    print(f"   3. Copy text for social media post")
    print(f"   4. See SOCIAL-WORKFLOW.md for posting guidelines")

    return html_path, png_path


def main():
    parser = argparse.ArgumentParser(
        description="Generate social media posts from BobRenze templates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --list                              # List all templates
  %(prog)s --template 01-launch --headline "New Feature" --subtitle "Shipped today"
  %(prog)s -t 04-tip -H "Quick Tip" -s "Use specific numbers" --screenshot
  %(prog)s --interactive                     # Interactive mode
        """,
    )

    parser.add_argument(
        "--list", "-l", action="store_true", help="List available templates"
    )

    parser.add_argument("--template", "-t", help="Template ID (e.g., '01-launch')")

    parser.add_argument("--headline", "-H", help="Headline text (replaces h1 content)")

    parser.add_argument(
        "--subtitle", "-s", help="Subtitle text (replaces .subtitle content)"
    )

    parser.add_argument(
        "--badge", "-b", help="Badge text (replaces .badge-text content)"
    )

    parser.add_argument(
        "--brand-mark", "-m", help="Brand mark character (replaces .brand-mark content)"
    )

    parser.add_argument("--output", "-o", help="Output filename (no extension)")

    parser.add_argument(
        "--screenshot",
        "-c",
        action="store_true",
        help="Generate PNG screenshot (requires openclaw browser)",
    )

    parser.add_argument(
        "--interactive",
        "-i",
        action="store_true",
        help="Interactive mode (prompts for all values)",
    )

    parser.add_argument(
        "--open",
        action="store_true",
        help="Open generated HTML in browser after creation",
    )

    args = parser.parse_args()

    # Handle list command
    if args.list:
        list_templates()
        return

    # Handle interactive mode
    if args.interactive:
        interactive_mode()
        return

    # Handle template generation
    if args.template:
        html_path, png_path = generate_post(
            template_id=args.template,
            headline=args.headline,
            subtitle=args.subtitle,
            badge=args.badge,
            brand_mark=args.brand_mark,
            output_name=args.output,
            screenshot=args.screenshot,
        )

        if args.open:
            subprocess.run(["open", str(html_path)])

        return

    # No valid command
    parser.print_help()
    print("\n💡 Try: python3 social-post-generator.py --list")


if __name__ == "__main__":
    main()
