  * [GitHub Issues](https://docs.github.com/en/issues "GitHub Issues")/
  * [Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects "Projects")/
  * [Automating projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project "Automating projects")/
  * [Archiving items automatically](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/archiving-items-automatically "Archiving items automatically")


# Archiving items automatically
You can configure your project's built-in workflows to automatically archive items that match a filter.
## In this article
  * [About automatically archiving items](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/archiving-items-automatically#about-automatically-archiving-items)
  * [Configuring automatic archiving in your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/archiving-items-automatically#configuring-automatic-archiving-in-your-project)
  * [Further reading](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/archiving-items-automatically#further-reading)


## [About automatically archiving items](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/archiving-items-automatically#about-automatically-archiving-items)
You can configure your project's built-in workflows to automatically archive items. Archiving items helps you improve focus by removing old items from your project views. An archived item retains all of its custom field data and can be viewed or restored from the archive page.
The auto-archive workflow supports a subset of filters. You can use the following filters when configuring your workflow.
Qualifier | Possible values  
---|---  
`is` |  `open`, `closed`, `merged`, `draft`, `issue`, `pr`  
`reason` |  `completed`, `reopened`, `"not planned"`  
`updated` |  `<@today-_14_d`(the last 14 days),`<@today-_3_w`(the last 3 weeks),`<@today-_1_m`(the last month)  
GitHub marks an issue or pull request as updated when it is:
  * Created
  * Reopened
  * Edited
  * Commented
  * Labeled
  * Assignees are updated
  * Milestones are updated
  * Transferred to another repository


Additionally, items are also marked as updated when field values in your project are changed.
When you enable automatic archiving for issues or pull requests, items in your project that already meet your criteria will also be archived. There may be some delay in archiving large numbers of items that already meet the criteria.
Your project can contain up to 50,000 items across both active views and the archive page. Once that limit has been reached, you will need to delete items from your project to free up more space. For more information on permanently deleting items, see [Archiving items from your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/archiving-items-from-your-project#deleting-items).
## [Configuring automatic archiving in your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/archiving-items-automatically#configuring-automatic-archiving-in-your-project)
  1. Navigate to your project.
  2. In the top-right, click 
![Screenshot showing a project's menu bar. The menu icon is highlighted with an orange outline.](https://docs.github.com/assets/cb-789/images/help/projects-v2/open-menu.png)
  3. In the menu, click 
  4. In the "Default workflows" list, click **Auto-archive items**.
  5. In the top right, click **Edit**.
![Screenshot showing a project's menu bar. The "Edit" button is highlighted with an orange rectangle.](https://docs.github.com/assets/cb-4809/images/help/projects-v2/workflow-start-editing.png)
  6. In the "Filters" field, type the filter criteria you want to use to automatically archive items. You can only use the `is`, `reason`, and `updated` filters.
  7. To save your changes and enable the workflow, click **Save and turn on workflow**.


## [Further reading](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/archiving-items-automatically#further-reading)
  * [Archiving items from your project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/managing-items-in-your-project/archiving-items-from-your-project)
  * [Using the built-in automations](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations)


