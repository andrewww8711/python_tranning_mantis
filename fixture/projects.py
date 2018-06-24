from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('td.menu:nth-child(1) > a:nth-child(7)').click()
        wd.find_element_by_link_text("Manage Projects").click()

    def create_project(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            self.open_project_page()
        wd.find_element_by_css_selector('input.button-small[value="Create New Project"]').click()
        wd.find_element_by_css_selector('input[name = "name"]').send_keys("project1")
        wd.find_element_by_css_selector('textarea:nth-child(1)').send_keys("description1")
        wd.find_element_by_css_selector('input[value="Add Project"]').send_keys("description1")

    def get_projec_list(self):
        wd = self.app.wd
        self.open_project_page()
        self.group_list = []
        for element in wd.find_elements_by_xpath("//*[@class='width100' and contains (text(), 'row-1')]"):
        #for element in wd.find_elements_by_css_selector('table.width100:nth-child(6) > tbody:nth-child(1)>tr.row-1'):# \
                #or wd.find_elements_by_css_selector('table.width100:nth-child(6) > tbody:nth-child(1)>tr.row-2'):
            cells = element.find_elements_by_css_selector('td')
            name = cells[0].text
            status = cells[1].text
            self.group_list.append(Project(name=name, status=status))
        return list(self.group_list)

    def count(self):
        wd = self.app.wd
        self.open_project_page()
        project_table = wd.find_elements_by_css_selector("table.width100:nth-child(6)")
        return len(project_table.wd.find_elements_by_css_selector("td"))
