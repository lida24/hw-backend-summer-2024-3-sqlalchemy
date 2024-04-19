from typing import TYPE_CHECKING

from sqlalchemy import select

from app.admin.models import AdminModel, Admin
from app.base.base_accessor import BaseAccessor

if TYPE_CHECKING:
    from app.web.app import Application


class AdminAccessor(BaseAccessor):
    async def connect(self, app: "Application") -> None:
        await super().connect(app)
        await self.create_admin(email=self.app.config.admin.email, password=self.app.config.admin.password)

    async def get_by_email(self, email: str) -> AdminModel | None:
        query = select(AdminModel).where(AdminModel.email == email)

        async with self.app.database.session() as session:
            admin: AdminModel | None = await session.scalar(query)

        return admin

    async def create_admin(self, email: str, password: str) -> AdminModel:
        admin = AdminModel(email=email, password=Admin.hash_password(password))

        async with self.app.database.session() as session:
            session.add(admin)
            await session.commit()

        return admin
