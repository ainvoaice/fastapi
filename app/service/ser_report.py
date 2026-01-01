# app/services/report_service.py
import csv
import io
from datetime import datetime
from app.db.models.m_report import Report
from app.db.repo.repo_report import ReportRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func


class ReportService:

    @staticmethod
    async def upload_csv(
        db: AsyncSession,
        file_bytes: bytes,
    ) -> None:
        text = file_bytes.decode("utf-8")
        reader = csv.DictReader(io.StringIO(text))

        reports: list[Report] = []

        for row in reader:
            content = f"""
                        Lead owner is {row['Lead Owner']}.
                        Source is {row['Source']}.
                        Deal stage is {row['Deal Stage']}.
                        Account ID is {row['Account Id']}.
                        Contact name is {row['First Name']} {row['Last Name']}.
                        Company name is {row['Company']}.
                    """.strip()
            report = Report(
                date=datetime.strptime(row["Date"], "%m/%d/%Y").date(),
                lead_owner=row["Lead Owner"],
                source=row["Source"],
                deal_stage=row["Deal Stage"],
                account_id=row["Account Id"],
                first_name=row["First Name"],
                last_name=row["Last Name"],
                company=row["Company"],
                content=content,
            )
            reports.append(report)

        await ReportRepository.bulk_insert(db, reports)

    @staticmethod
    async def list_reports(
        db: AsyncSession,
    ):
        return await ReportRepository.list_reports(db)

    @staticmethod
    async def reports_pagination(
        db: AsyncSession,
        page: int,
        page_size: int,
        query: str | None = None,
        sort_by: str = "created_at",
        sort_order: str = "desc",
    ):
        stmt = select(Report)

        if query:
            stmt = stmt.where(Report.name.ilike(f"%{query}%"))

        column = getattr(Report, sort_by, Report.created_at)
        stmt = stmt.order_by(column.desc() if sort_order == "desc" else column.asc())

        total_stmt = select(func.count()).select_from(stmt.subquery())
        total = (await db.execute(total_stmt)).scalar()

        stmt = stmt.offset((page - 1) * page_size).limit(page_size)
        items = (await db.execute(stmt)).scalars().all()

        return {
            "items": items,
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": (total + page_size - 1) // page_size,
        }