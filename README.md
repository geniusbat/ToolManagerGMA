# ToolManagerGMA
Tool Manager GMA is a web application inted to be used as a pseudo-ERP for machining and industrial companies that have to manage the different tools/pieces and machines 
of the workshop.

It allows the user to trace tools as they are used, counting the hours it has been used, the machine it can be used for, the different specs and extra data. Manage the different
orders, from clients and suppliers, and the dates the orders and invoices are generated.


## Concepts
-Machine: Machines populate the workshop, they create the products for the company given some materials and tools.

-Tool: The bits and pieces the machine use to cut the material. They are asigned to a machine thus they shouldn't be used for other ones.

-Archetype tool: Sometimes we encounter that we buy/use similar tools (ie: We buy the same tool multiple times as each one should be used for a machine), to automate the 
creation of tools and manage large amounts of them we use archetypes, that define the base properties of the tools, from there, when creating a tool the user can define
that it is an archetype and it will inherit the data.

-Supplier order: The order to the supplier of new tools.

-Client order: The request from a client of products. 

-Client order item: The products associated to the client order.
