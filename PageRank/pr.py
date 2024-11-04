class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []
        self.pagerank = 1.0  # Initialize PageRank to 1.0

    # Add child and parent relationships
    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parents.append(self)


class Graph:
    def __init__(self):
        self.nodes = []

    # Add node to the graph
    def add_node(self, node):
        self.nodes.append(node)

    # Run one iteration of the PageRank algorithm
    def PageRank_one_iter(self, damping_factor):
        for node in self.nodes:
            node.update_pagerank(damping_factor, len(self.nodes))


def update_pagerank(self, damping_factor, num_nodes):
    pagerank_sum = sum((parent.pagerank / len(parent.children)) for parent in self.parents)
    random_walk = damping_factor / num_nodes
    self.pagerank = random_walk + (1 - damping_factor) * pagerank_sum

# Attach the method to the Node class
Node.update_pagerank = update_pagerank

# Example to construct a graph with the structure from the image (graph_1.txt)
def main():
    # Initialize the graph
    graph = Graph()

    # Create nodes for the graph
    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    node4 = Node("4")
    node5 = Node("5")
    node6 = Node("6")

    # Add child-parent relationships as shown in the image
    node1.add_child(node2)
    node2.add_child(node3)
    node3.add_child(node4)
    node4.add_child(node5)
    node5.add_child(node6)

    # Add nodes to the graph
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_node(node4)
    graph.add_node(node5)
    graph.add_node(node6)

    # Set damping factor to 0.15
    damping_factor = 0.15

    # Run multiple iterations of PageRank to allow convergence
    num_iterations = 100
    for i in range(num_iterations):
        graph.PageRank_one_iter(damping_factor)

    # Display the final PageRank for each node
    for node in graph.nodes:
        print(f"Node {node.name} PageRank: {node.pagerank:.4f}")

if __name__ == "__main__":
    main()
