from sqlalchemy import text


class SubjectTable:
    def __init__(self, engine):
        self.engine = engine

    def create(self, title):
        query = (
            "INSERT INTO subject (subject_title) "
            "VALUES (:title) "
            "RETURNING subject_id, subject_title"
        )

        with self.engine.begin() as conn:
            result = conn.execute(
                text(query),
                {"title": title},
            )
            return result.mappings().first()

    def update(self, subject_id, new_title):
        query = (
            "UPDATE subject "
            "SET subject_title = :title "
            "WHERE subject_id = :id"
        )

        with self.engine.begin() as conn:
            result = conn.execute(
                text(query),
                {
                    "id": subject_id,
                    "title": new_title,
                },
            )
            return result.rowcount

    def delete(self, subject_id):
        query = (
            "DELETE FROM subject "
            "WHERE subject_id = :id"
        )

        with self.engine.begin() as conn:
            conn.execute(
                text(query),
                {"id": subject_id},
            )

    def exists(self, subject_id):
        query = (
            "SELECT 1 FROM subject "
            "WHERE subject_id = :id"
        )

        with self.engine.connect() as conn:
            result = conn.execute(
                text(query),
                {"id": subject_id},
            )
            return result.first() is not None
