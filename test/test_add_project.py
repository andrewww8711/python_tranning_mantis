from fixture.projects import ProjectHelper

def test_add_project(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")
    old_list_projects = app.project.get_projec_list()
    app.project.create_project()
    assert len(old_list_projects) + 1 == app.project.count()
    #app.project.open_project_page()


