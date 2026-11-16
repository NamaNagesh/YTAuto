"""
YTAuto Main Entry Point.
"""
import argparse
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from langgraph_workflow import build_workflow, run_workflow

def main():
    parser = argparse.ArgumentParser(description="YTAuto - YouTube Video Automation Workflow")
    parser.add_argument("--prompt", type=str, required=True, help="Software topic prompt")
    parser.add_argument("--checkpoint", action="store_true", help="Enable checkpointing")
    args = parser.parse_args()
    print(f"[YTAuto] Starting workflow for topic: {args.prompt}")
    try:
        result = run_workflow(args.prompt, use_checkpoint=args.checkpoint)
        print("[YTAuto] Workflow completed!")
        print(f"[YTAuto] Status: {result.get('status')}")
        print(f"[YTAuto] Videos: {len(result.get('video_playlist', []))}")
    except Exception as exc:
        print(f"[YTAuto] Failed: {exc}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
