  * [GitHub Copilot](https://docs.github.com/en/copilot "GitHub Copilot")/
  * [Copilot Chat Cookbook](https://docs.github.com/en/copilot/copilot-chat-cookbook "Copilot Chat Cookbook")/
  * [Refactoring code](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code "Refactoring code")/
  * [Simplify inheritance hierarchies](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/simplifying-complex-inheritance-hierarchies "Simplify inheritance hierarchies")


# Simplifying complex inheritance hierarchies
Copilot Chat can help you to refactor code to avoid classes with multiple layers of inheritance.
## In this article
  * [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/simplifying-complex-inheritance-hierarchies#example-scenario)
  * [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/simplifying-complex-inheritance-hierarchies#example-prompt)
  * [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/simplifying-complex-inheritance-hierarchies#example-response)
  * [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/simplifying-complex-inheritance-hierarchies#further-reading)


Deep inheritance hierarchies, or improper use of inheritance, can lead to code that is hard to maintain, making it difficult to follow relationships between classes, or to extend them without causing breakage.
Copilot Chat can suggest refactoring inheritance-based designs into more flexible composition-based designs (favoring composition over inheritance). It can also recommend applying patterns like Strategy or Decorator to make the system more extensible without adding complexity to the inheritance structure.
## [Example scenario](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/simplifying-complex-inheritance-hierarchies#example-scenario)
The following C# code has a deep inheritance hierarchy where each class builds on the previous one. The result is a long chain of inheritance that makes it difficult to know what properties each class has.
A multi-level inheritance hierarchy like this can be difficult to understand, modify, and extend.
```
public class Employee
{
    public string Name { get; set; }
    public int EmployeeID { get; set; }
}

public class Manager : Employee
{
    public int NumberOfTeams { get; set; }
}

public class SeniorManager : Manager
{
    public string Region { get; set; }
}

public class Director : SeniorManager
{
    public int NumberOfDepartments { get; set; }
}

public class VicePresident : Director
{
    public string Division { get; set; }
}

public class President : VicePresident
{
    public string Company { get; set; }
}

```

## [Example prompt](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/simplifying-complex-inheritance-hierarchies#example-prompt)
In this situation you might decide to use a parent `Employee` class whose properties other classes should inherit, but to avoid any other inheritance by defining all other properties separately for each class.
`Refactor this code so that classes only inherit the properties of the Employee class. All of the other properties that each class currently inherits should instead be declared independently in each class definition.`
## [Example response](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/simplifying-complex-inheritance-hierarchies#example-response)
The following response is an example. Copilot Chat responses are non-deterministic, so you may get a different response from the one shown here.
Copilot suggests the following code:
```
public class Employee
{
    public string Name { get; set; }
    public int EmployeeID { get; set; }
}

public class Manager : Employee
{
    public int NumberOfTeams { get; set; }
}

public class SeniorManager : Employee
{
    public int NumberOfTeams { get; set; }
    public string Region { get; set; }
}

public class Director : Employee
{
    public int NumberOfTeams { get; set; }
    public string Region { get; set; }
    public int NumberOfDepartments { get; set; }
}

public class VicePresident : Employee
{
    public int NumberOfTeams { get; set; }
    public string Region { get; set; }
    public int NumberOfDepartments { get; set; }
    public string Division { get; set; }
}

public class President : Employee
{
    public int NumberOfTeams { get; set; }
    public string Region { get; set; }
    public int NumberOfDepartments { get; set; }
    public string Division { get; set; }
    public string Company { get; set; }
}

```

## [Further reading](https://docs.github.com/en/copilot/copilot-chat-cookbook/refactoring-code/simplifying-complex-inheritance-hierarchies#further-reading)
  * [Prompt engineering for Copilot Chat](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
  * [Best practices for using GitHub Copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)


