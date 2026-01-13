"""Simple CLI to generate AdaptaNote activities."""
from __future__ import annotations

import argparse
from adaptanote import format_activity, generate_activity


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gerador simples de atividades adaptadas AdaptaNote",
    )
    parser.add_argument("topic", help="Tema central da atividade")
    parser.add_argument(
        "--level",
        type=int,
        default=1,
        choices=[1, 2, 3],
        help="Nível de adaptação (1, 2 ou 3)",
    )
    parser.add_argument(
        "--no-instructions",
        action="store_true",
        help="Não incluir instruções para aluno e professor",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    activity = generate_activity(
        topic=args.topic,
        level=args.level,
        include_instructions=not args.no_instructions,
    )
    print(format_activity(activity))


if __name__ == "__main__":
    main()
