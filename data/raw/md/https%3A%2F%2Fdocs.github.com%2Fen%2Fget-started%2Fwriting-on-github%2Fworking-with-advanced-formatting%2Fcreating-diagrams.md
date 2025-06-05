  * [Get started](https://docs.github.com/en/get-started "Get started")/
  * [Writing on GitHub](https://docs.github.com/en/get-started/writing-on-github "Writing on GitHub")/
  * [Work with advanced formatting](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting "Work with advanced formatting")/
  * [Create diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams "Create diagrams")


# Creating diagrams
Create diagrams to convey information through charts and graphs
## Who can use this feature?
Markdown can be used in the GitHub web interface.
## In this article
  * [About creating diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#about-creating-diagrams)
  * [Creating Mermaid diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams)
  * [Creating GeoJSON and TopoJSON maps](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-geojson-and-topojson-maps)
  * [Creating STL 3D models](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-stl-3d-models)


## [About creating diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#about-creating-diagrams)
You can create diagrams in Markdown using four different syntaxes: mermaid, geoJSON, topoJSON, and ASCII STL. Diagram rendering is available in GitHub Issues, GitHub Discussions, pull requests, wikis, and Markdown files.
## [Creating Mermaid diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-mermaid-diagrams)
Mermaid is a Markdown-inspired tool that renders text into diagrams. For example, Mermaid can render flow charts, sequence diagrams, pie charts and more. For more information, see the [Mermaid documentation](https://mermaid-js.github.io/mermaid/#/).
To create a Mermaid diagram, add Mermaid syntax inside a fenced code block with the `mermaid` language identifier. For more information about creating code blocks, see [Creating and highlighting code blocks](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks).
For example, you can create a flow chart by specifying values and arrows.
```
Here is a simple flow chart:

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

```

![Screenshot of a rendered Mermaid flow chart with four lavender boxes labeled A, B, C, and D. Arrows extend from A to B, B to D, A to C, and C to D.](https://docs.github.com/assets/cb-46019/images/help/writing/mermaid-flow-chart.png)
You may observe errors if you run a third-party Mermaid plugin when using Mermaid syntax on GitHub.
### [Checking your version of Mermaid](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#checking-your-version-of-mermaid)
To ensure GitHub supports your Mermaid syntax, check the Mermaid version currently in use.
```
```mermaid
  info
```

```

## [Creating GeoJSON and TopoJSON maps](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-geojson-and-topojson-maps)
You can use GeoJSON or TopoJSON syntax to create interactive maps. To create a map, add GeoJSON or TopoJSON inside a fenced code block with the `geojson` or `topojson` syntax identifier. For more information, see [Creating and highlighting code blocks](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks).
### [Using GeoJSON](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#using-geojson)
For example, you can create a map by specifying coordinates.
```
```geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 1,
      "properties": {
        "ID": 0
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
              [-90,35],
              [-90,30],
              [-85,30],
              [-85,35],
              [-90,35]
          ]
        ]
      }
    }
  ]
}
```

```

![Screenshot of a rendered GeoJSON map of the southeastern United States with a purple rectangular overlay over parts of Alabama and Mississippi.](https://docs.github.com/assets/cb-304239/images/help/writing/fenced-geojson-rendered-map.png)
### [Using TopoJSON](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#using-topojson)
For example, you can create a TopoJSON map by specifying coordinates and shapes.
```
```topojson
{
  "type": "Topology",
  "transform": {
    "scale": [0.0005000500050005, 0.00010001000100010001],
    "translate": [100, 0]
  },
  "objects": {
    "example": {
      "type": "GeometryCollection",
      "geometries": [
        {
          "type": "Point",
          "properties": {"prop0": "value0"},
          "coordinates": [4000, 5000]
        },
        {
          "type": "LineString",
          "properties": {"prop0": "value0", "prop1": 0},
          "arcs": [0]
        },
        {
          "type": "Polygon",
          "properties": {"prop0": "value0",
            "prop1": {"this": "that"}
          },
          "arcs": [[1]]
        }
      ]
    }
  },
  "arcs": [[[4000, 0], [1999, 9999], [2000, -9999], [2000, 9999]],[[0, 0], [0, 9999], [2000, 0], [0, -9999], [-2000, 0]]]
}
```

```

![Screenshot of a rendered TopoJSON map of Indonesia, Singapore, and Malaysia with a blue point, a purple rectangular overlay, and blue zigzag lines.](https://docs.github.com/assets/cb-434182/images/help/writing/fenced-topojson-rendered-map.png)
For more information on working with `.geojson` and `.topojson` files, see [Working with non-code files](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files#mapping-geojson-files-on-github).
## [Creating STL 3D models](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams#creating-stl-3d-models)
You can use ASCII STL syntax directly in markdown to create interactive 3D models. To display a model, add ASCII STL syntax inside a fenced code block with the `stl` syntax identifier. For more information, see [Creating and highlighting code blocks](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks).
For example, you can create a simple 3D model:
```
```stl
solid cube_corner
  facet normal 0.0 -1.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 1.0 0.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
  facet normal 0.0 0.0 -1.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 1.0 0.0 0.0
    endloop
  endfacet
  facet normal -1.0 0.0 0.0
    outer loop
      vertex 0.0 0.0 0.0
      vertex 0.0 0.0 1.0
      vertex 0.0 1.0 0.0
    endloop
  endfacet
  facet normal 0.577 0.577 0.577
    outer loop
      vertex 1.0 0.0 0.0
      vertex 0.0 1.0 0.0
      vertex 0.0 0.0 1.0
    endloop
  endfacet
endsolid
```

```

![Screenshot of a 3D model of a blue pyramid on a grid of black lines. Options "Wireframe", "Surface Angle", or "Solid" appear at bottom.](https://docs.github.com/assets/cb-123217/images/help/writing/fenced-stl-rendered-object.png)
For more information on working with `.stl` files, see [Working with non-code files](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files#3d-file-viewer).
