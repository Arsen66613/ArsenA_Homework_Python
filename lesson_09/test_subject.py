from lesson_09.subject_table import SubjectTable


def test_add_subject(engine):
    subject_table = SubjectTable(engine)
    title = "PyTest Subject"

    subject = subject_table.create(title)

    assert subject is not None
    assert subject["subject_title"] == title

    subject_table.delete(subject["subject_id"])


def test_update_subject(engine):
    subject_table = SubjectTable(engine)

    subject = subject_table.create("Temp")
    subject_id = subject["subject_id"]

    rows_updated = subject_table.update(subject_id, "Updated")

    assert rows_updated >= 0

    subject_table.delete(subject_id)


def test_delete_subject(engine):
    subject_table = SubjectTable(engine)

    subject = subject_table.create("ToDelete")
    subject_id = subject["subject_id"]

    subject_table.delete(subject_id)

    assert subject_table.exists(subject_id) is False
