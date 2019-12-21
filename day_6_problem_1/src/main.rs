use std::collections::HashMap;

pub struct Tree<T> {
    nodes: Vec<Node<T>>,
    hashmap: HashMap<Node<T>, usize>::new(),
}

impl<T> Tree<T> {
    pub fn add_node(&mut self, node: Node<T>) -> NodeId {
        if !self.hashmap.contains_key(node) {

        }
        self.hashmap.get
    }

    pub fn new_node(&mut self, data: T) -> NodeId {
        let next_index = self.nodes.len();

        self.nodes.push(Node {
            parent:             None,
            previous_sibling:   None,
            next_sibling:       None,
            first_child:        None,
            last_child:         None,
            data:               data,
        });

        NodeId { index: next_index }
    }
}

pub struct Node<T> {
    parent:             Option<NodeId>,
    previous_sibling:   Option<NodeId>,
    next_sibling:       Option<NodeId>,
    first_child:        Option<NodeId>,
    last_child:         Option<NodeId>,

    // The data stored within the node
    pub data: T,
}

pub struct NodeId {
    index: usize,
}

fn main() {
    let mut foo: Tree<&str> = Tree { nodes: Vec::new() };
    foo.new_node("foo");
}
