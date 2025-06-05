  * [GitHub Issues](https://docs.github.com/en/issues "GitHub Issues")/
  * [Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects "Projects")/
  * [Automating projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project "Automating projects")/
  * [Adding items automatically](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically "Adding items automatically")


# Adding items automatically
You can configure your project's built-in workflows to automatically add items from repositories that match a filter.
## In this article
  * [About automatically adding items](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically#about-automatically-adding-items)
  * [Configuring the auto-add workflow in your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically#configuring-the-auto-add-workflow-in-your-project)
  * [Duplicating the auto-add workflow](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically#duplicating-the-auto-add-workflow)
  * [Further reading](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically#further-reading)


## [About automatically adding items](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically#about-automatically-adding-items)
You can configure your project's built-in workflows to automatically add new items as they are created or updated in a repository. You can define a filter to only add items that meet your criteria. You can also create multiple auto-add workflows, each workflow can have a unique filter and target a different repository.
When you enable the auto-add workflow, existing items matching your criteria will not be added. The workflow will add items when created or updated if the item matches your filter. For more information on manually adding items, see [Adding items to your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/adding-items-to-your-project#bulk-adding-issues-and-pull-requests).
The auto-add workflow supports a subset of filters. You can use the following filters when configuring your workflow.
Qualifier | Possible values  
---|---  
`is` | open, closed, merged, draft, issue, pr  
`label` | "label name"  
`reason` | completed, reopened, "not planned"  
`assignee` | GitHub username  
`no` | label, assignee, reason  
All filters, other than `no`, support negation. For example, you could use `-label:bug` to add issues that do not have the "bug" label.
The auto-add workflow is limited per plan.
Product | Maximum auto-add workflows  
---|---  
GitHub Free | 1  
GitHub Pro | 5  
GitHub Team | 5  
GitHub Enterprise Cloud | 20  
GitHub Enterprise Server | 20  
## [Configuring the auto-add workflow in your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically#configuring-the-auto-add-workflow-in-your-project)
  1. Navigate to your project.
  2. In the top-right, click 
![Screenshot showing a project's menu bar. The menu icon is highlighted with an orange outline.](https://docs.github.com/assets/cb-789/images/help/projects-v2/open-menu.png)
  3. In the menu, click 
  4. In the "Default workflows" list, click **Auto-add to project** or one of the auto-add workflows you have previously duplicated.
  5. To start editing the workflow, in the top right, click **Edit**.
![Screenshot showing the workflow menu bar. The "Edit" button is highlighted with an orange rectangle.](https://docs.github.com/assets/cb-4809/images/help/projects-v2/workflow-start-editing.png)
  6. Under "Filters", select the repository you want to add items from.
  7. Next to the repository selection, type the filter criteria you want items to match before they are automatically added to your project.
  8. To enable the new workflow, click **Save and turn on workflow**.


## [Duplicating the auto-add workflow](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically#duplicating-the-auto-add-workflow)
You can create additional duplicates of the auto-add workflow, up to a maximum defined for your plan (see the table earlier in this article). Each workflow can target a different repository. You can target the same repository with multiple workflows if the filter is unique for each workflow.
Once you have duplicated a workflow, you can click **Edit** to start making changes to it. For more information, see [Configuring the auto-add workflow in your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically#configuring-the-auto-add-workflow-in-your-project).
  1. Navigate to your project.
  2. In the top-right, click 
![Screenshot showing a project's menu bar. The menu icon is highlighted with an orange outline.](https://docs.github.com/assets/cb-789/images/help/projects-v2/open-menu.png)
  3. In the menu, click 
  4. In the list of workflows, next to "Auto-add to project" click 
![Screenshot showing the list of workflows. The ellipsis button next to the auto-add workflow is highlighted with an orange rectangle.](https://docs.github.com/assets/cb-8504/images/help/projects-v2/workflow-add-menu.png)
  5. In the menu, click 
  6. To save your new workflow, when prompted, type the name you want to use for the new workflow.


## [Further reading](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/adding-items-automatically#further-reading)
  * [Archiving items from your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/archiving-items-from-your-project)
  * [Using the built-in automations](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)


