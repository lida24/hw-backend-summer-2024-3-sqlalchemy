from collections.abc import Iterable, Sequence

from sqlalchemy import select

from app.base.base_accessor import BaseAccessor
from app.quiz.models import (
    AnswerModel,
    QuestionModel,
    ThemeModel,
)


class QuizAccessor(BaseAccessor):
    async def create_theme(self, title: str) -> ThemeModel:
        theme = ThemeModel(title=title)

        async with self.app.database.session() as session:
            session.add(theme)
            await session.commit()

        return theme

    async def get_theme_by_title(self, title: str) -> ThemeModel | None:
        query = select(ThemeModel).where(ThemeModel.title == title)

        async with self.app.database.session() as session:
            theme: ThemeModel | None = await session.scalar(query)

        return theme

    async def get_theme_by_id(self, id_: int) -> ThemeModel | None:
        query = select(ThemeModel).where(ThemeModel.id == id_)

        async with self.app.database.session() as session:
            theme: ThemeModel | None = await session.scalar(query)

        return theme

    async def list_themes(self) -> Sequence[ThemeModel]:
        query = select(ThemeModel)

        async with self.app.database.session() as session:
            themes: Sequence[ThemeModel] = await session.scalars(query)

        return themes

    async def create_question(
        self, title: str, theme_id: int, answers: Iterable[AnswerModel]
    ) -> QuestionModel:
        question = QuestionModel(title=title, theme_id=theme_id, answers=answers)

        async with self.app.database.session() as session:
            session.add(question)
            await session.commit()

        return question

    async def get_question_by_title(self, title: str) -> QuestionModel | None:
        query = select(QuestionModel).where(QuestionModel.title == title)

        async with self.app.database.session() as session:
            question: QuestionModel | None = await session.scalar(query)

        return question

    async def list_questions(
        self, theme_id: int | None = None
    ) -> Sequence[QuestionModel]:
        query = select(QuestionModel) if not theme_id else select(QuestionModel).where(QuestionModel.theme_id == theme_id)

        async with self.app.database.session() as session:
            questions: Sequence[QuestionModel] = await session.scalars(query)

        return questions
