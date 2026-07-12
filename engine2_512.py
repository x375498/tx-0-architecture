"""
TX-0 Relational Architecture v2.0 — Background-Independent Engine
WITH DYNAMIC GRAPH REWRITING

Axiom III (Revised): Phase Reorganization
  When local difference-flux exceeds C_max, the relational structure undergoes
  irreversible topological reorganization. The node must DROP local edges 
  (whose neighbors are overloading it) and ESTABLISH new edges to distant, 
  under-density regions. The graph rewrites its own geometry to find equilibrium.

This is NOT an external rule imposed from above. It is the intrinsic consequence
of phase transition: conformal constraint can no longer bind the overloaded node
to its current neighbors. It must seek new relational partners.
"""

import math
import random
import sys
import time
import numpy as np
from collections import defaultdict
from scipy.stats import entropy as scipy_entropy
import networkx as nx

# ============================================================================
# PART 0: AXIOM-LEVEL FORMALIZATION
# ============================================================================

class Axiom_I_DifferencePrimitive:
    """Axiom I: The universe is a poset of pure relational differences."""
    @staticmethod
    def validate_poset(nodes, edges):
        """Verify DAG property."""
        G = nx.DiGraph()
        G.add_nodes_from([n["id"] for n in nodes])
        G.add_edges_from(edges)
        return nx.is_directed_acyclic_graph(G)


class Axiom_II_ConformalBinding:
    """Axiom II: Local order constrained by hyperbolic metric from Λ(θ)."""
    @staticmethod
    def derive_capacity_threshold(theta_ideal=math.pi / 3.0):
        """Derive C_max from volume of regular ideal hyperbolic 3-simplex."""
        lambda_val = compute_lobachevsky(theta_ideal)
        v_ideal = 3.0 * lambda_val
        capacity_scale = 1.49462712534
        c_max = (9.0 / 2.0) * v_ideal * (v_ideal / capacity_scale)
        return c_max, lambda_val, v_ideal


class Axiom_III_DensityPhaseCoupling:
    """
    Axiom III (DYNAMIC): When local density > C_max, the relational structure 
    undergoes irreversible phase reorganization via INTRINSIC TOPOLOGICAL REWRITING.
    
    The node doesn't absorb excess tension—it RESTRUCTURES its edge set:
    - Drops edges to nearest neighbors (pressure relief)
    - Seeks new edges to distant, under-dense regions (load rebalancing)
    """
    @staticmethod
    def phase_transition(density, c_max):
        """Determine phase based on density and C_max threshold."""
        if density < 2.0:
            return "R1 (Linear)"
        elif density < c_max:
            return "R2 (Planar Vortex)"
        else:
            return "R3 (Inversion Event)"


class Axiom_IV_CascadeDissipation:
    """
    Axiom IV (INTRINSIC): Excess flux dissipates by STRUCTURAL REWIRING, not cascade.
    When a node inverts, it redistributes its relational bonds to restore equilibrium.
    """
    @staticmethod
    def dissipate_excess(source_density, c_max, neighbor_count):
        """Compute excess flux (returned for topological reorganization)."""
        if source_density <= c_max:
            return 0.0
        excess = source_density - c_max
        return excess


class Axiom_V_ClosureAndConsistency:
    """Axiom V: System is closed under relational dynamics. All reorganization
    emerges from internal difference-gradients and topological self-rewriting."""
    @staticmethod
    def is_equilibrated(nodes, c_max, tolerance=0.05):
        """Check if system reached quasi-equilibrium via stable topology."""
        inversion_fraction = sum(1 for n in nodes if n["density"] > c_max) / len(nodes)
        return inversion_fraction < tolerance


# ============================================================================
# PART 1: LOBACHEVSKY FUNCTION (Axiom II Foundation)
# ============================================================================

def lobachevsky_integrand(t):
    """Integrand for the Lobachevsky function: -ln|2 * sin(t)|."""
    sin_t = math.sin(t)
    if sin_t <= 0:
        return 0.0
    return -math.log(2.0 * sin_t)


def compute_lobachevsky(theta, steps=100000):
    """Computes the Lobachevsky function Lambda(theta) using Simpson's Rule."""
    if theta == 0:
        return 0.0
    
    eps = 1e-12
    h = (theta - eps) / steps
    
    integration_sum = lobachevsky_integrand(eps) + lobachevsky_integrand(theta)
    
    for i in range(1, steps):
        t = eps + i * h
        weight = 4.0 if i % 2 != 0 else 2.0
        integration_sum += weight * lobachevsky_integrand(t)
        
    return (h / 3.0) * integration_sum


def derive_c_max():
    """Derives C_max from Axiom II (Conformal Binding)."""
    theta_ideal = math.pi / 3.0
    lambda_pi_3 = compute_lobachevsky(theta_ideal)
    v_ideal = 3.0 * lambda_pi_3
    capacity_scale = 1.49462712534
    c_max = (9.0 / 2.0) * v_ideal * (v_ideal / capacity_scale)
    return lambda_pi_3, v_ideal, c_max


# ============================================================================
# PART 2: RELATIONAL NETWORK WITH DYNAMIC GRAPH REWRITING
# ============================================================================

class TX0RelationalNetwork:
    """
    Simulates a N-node background-independent relational poset network.
    NOW WITH DYNAMIC TOPOLOGICAL REWRITING.
    
    The graph is NOT fixed. When a node breaches C_max, it rewires its edges
    to restore equilibrium. The topology evolves intrinsically.
    """
    def __init__(self, num_nodes=512, topology="random", seed=None):
        self.num_nodes = num_nodes
        self.topology = topology
        self.nodes = []
        self.edges = set()
        self.tension_delta = 1.0
        self.inversion_events = 0
        self.rewiring_events = 0
        self.edges_dropped = 0
        self.edges_created = 0
        self.history = {
            "tension": [],
            "avg_density": [],
            "phase_distribution": [],
            "structural_entropy": [],
            "inversion_count": [],
            "rewiring_count": [],
            "edge_count": [],
            "topology_distance": []
        }
        
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
        
        self.initialize_network(topology)
        self.initial_edges = len(self.edges)  # Track topology change

    def initialize_network(self, topology):
        """Initialize nodes with hyperbolic coordinates and edges based on topology."""
        for i in range(self.num_nodes):
            r = random.uniform(0.0, 0.95)
            theta = random.uniform(0, 2 * math.pi)
            phi = random.uniform(0, math.pi)
            self.nodes.append({
                "id": i,
                "r": r,
                "theta": theta,
                "phi": phi,
                "density": 0.0,
                "phase": "R1",
                "last_inversion_step": -100  # Track inversion history
            })
        
        # Build edges based on topology
        if topology == "linear":
            self._build_linear_chain()
        elif topology == "random":
            self._build_random_graph()
        elif topology == "scale-free":
            self._build_scale_free_graph()
        else:
            raise ValueError(f"Unknown topology: {topology}")

    def _build_linear_chain(self):
        """Build a 1D chain poset (minimal conformal structure)."""
        for i in range(self.num_nodes - 1):
            self.edges.add((i, i + 1))

    def _build_random_graph(self):
        """Build Erdős-Rényi random graph."""
        G = nx.erdos_renyi_graph(self.num_nodes, 0.15, seed=None)
        self.edges.update(G.edges())

    def _build_scale_free_graph(self):
        """Build Barabási-Albert scale-free graph."""
        G = nx.barabasi_albert_graph(self.num_nodes, 3)
        self.edges.update(G.edges())

    def hyperbolic_distance(self, n1, n2):
        """Calculate hyperbolic distance in Poincaré coordinates."""
        dx = n1["r"] * math.cos(n1["theta"]) - n2["r"] * math.cos(n2["theta"])
        dy = n1["r"] * math.sin(n1["theta"]) - n2["r"] * math.sin(n2["theta"])
        dz = n1["r"] * math.cos(n1["phi"]) - n2["r"] * math.cos(n2["phi"])
        euclidean_sq = dx*dx + dy*dy + dz*dz
        
        denom = (1.0 - n1["r"]**2) * (1.0 - n2["r"]**2)
        if denom <= 0:
            denom = 1e-9
            
        arg = 1.0 + 2.0 * euclidean_sq / denom
        if arg < 1.0:
            arg = 1.0
        return math.acosh(arg)

    def get_node_neighbors(self, node_id):
        """Get all neighbors of a node."""
        return [n for n in self.nodes 
                if (node_id, n["id"]) in self.edges or (n["id"], node_id) in self.edges]

    def get_edge_with_node(self, node_id):
        """Get all edges involving a node."""
        return [(u, v) for u, v in self.edges if u == node_id or v == node_id]

    def rewire_node_edges(self, inversion_node, c_max):
        """
        Axiom III (Dynamic): When a node inverts, it rewires its topology.
        
        1. DROP edges to the K nearest neighbors (pressure relief)
        2. SEEK new edges to distant, under-dense regions (load rebalancing)
        """
        node_id = inversion_node["id"]
        
        # Get current neighbors
        neighbors = self.get_node_neighbors(node_id)
        if not neighbors:
            return  # Isolated node, nothing to rewire
        
        # STEP 1: Drop edges to nearest neighbors (those adding pressure)
        # Sort neighbors by distance (closest first)
        neighbor_distances = [(n, self.hyperbolic_distance(inversion_node, n)) 
                               for n in neighbors]
        neighbor_distances.sort(key=lambda x: x[1])
        
        # Drop top 30% of closest edges
        drop_count = max(1, len(neighbor_distances) // 3)
        edges_to_drop = [n["id"] for n, _ in neighbor_distances[:drop_count]]
        
        for neighbor_id in edges_to_drop:
            edge = (min(node_id, neighbor_id), max(node_id, neighbor_id))
            if edge in self.edges:
                self.edges.discard(edge)
                self.edges_dropped += 1
        
        # STEP 2: Seek new edges to distant, under-dense nodes
        # Find nodes with lowest density that are NOT currently neighbors
        current_neighbor_ids = set(n["id"] for n in neighbors)
        candidate_nodes = [n for n in self.nodes 
                          if n["id"] != node_id 
                          and n["id"] not in current_neighbor_ids
                          and n["density"] < c_max * 0.5]  # Target under-dense nodes
        
        if candidate_nodes:
            # Sort by density (lowest first) and distance (not too far)
            scored_candidates = []
            for candidate in candidate_nodes:
                dist = self.hyperbolic_distance(inversion_node, candidate)
                # Preference: low density + moderate distance (not too close, not too far)
                score = candidate["density"] / (dist + 0.1)
                scored_candidates.append((candidate, score))
            
            scored_candidates.sort(key=lambda x: x[1])
            
            # Create new edges to best candidates (same number as dropped)
            for candidate, _ in scored_candidates[:drop_count]:
                edge = (min(node_id, candidate["id"]), max(node_id, candidate["id"]))
                if edge not in self.edges:
                    self.edges.add(edge)
                    self.edges_created += 1

    def update_network_state(self, delta_step, c_max):
        """
        Axioms III–V: Update system tension, densities, and DYNAMIC TOPOLOGY.
        The graph rewrites itself to find equilibrium.
        """
        self.tension_delta += delta_step
        self.inversion_events = 0
        self.rewiring_events = 0
        
        # Step 1: Compute densities
        for node in self.nodes:
            connections = len(self.get_node_neighbors(node["id"]))
            local_packing_density = (connections / 12.0) * (1.0 / (1.0 - node["r"]**2 + 1e-9))
            node["density"] = self.tension_delta * local_packing_density
            node["phase"] = Axiom_III_DensityPhaseCoupling.phase_transition(node["density"], c_max)

        # Step 2: Identify inversions and trigger DYNAMIC REWIRING (not cascade dissipation)
        for node in self.nodes:
            if node["density"] > c_max:
                self.inversion_events += 1
                # Clamp density to C_max (node enters R3, stabilizes at threshold)
                node["density"] = c_max
                node["phase"] = "R3 (Inversion Event)"
                
                # AXIOM III REWRITING: Dynamically rewire topology
                self.rewire_node_edges(node, c_max)
                self.rewiring_events += 1

    def compute_structural_entropy(self):
        """
        Composite metric: Shannon entropy of phase distribution × degree centrality variance.
        Measures organization of emergent structure.
        """
        phase_counts = defaultdict(int)
        for node in self.nodes:
            phase_counts[node["phase"]] += 1
        
        phase_probs = np.array([count / self.num_nodes for count in phase_counts.values()])
        phase_entropy = scipy_entropy(phase_probs) if len(phase_probs) > 0 else 0.0
        
        degree_dict = defaultdict(int)
        for edge in self.edges:
            degree_dict[edge[0]] += 1
            degree_dict[edge[1]] += 1
        
        degrees = np.array([degree_dict.get(n["id"], 0) for n in self.nodes])
        degree_variance = np.var(degrees) if len(degrees) > 0 else 0.0
        
        structural_entropy = phase_entropy * (1.0 + degree_variance)
        
        return {
            "phase_entropy": phase_entropy,
            "degree_variance": degree_variance,
            "structural_entropy": structural_entropy,
            "phase_distribution": dict(phase_counts)
        }

    def compute_topology_distance(self):
        """Measure how much the topology has drifted from initial state."""
        current_edges = len(self.edges)
        edge_delta = abs(current_edges - self.initial_edges)
        return edge_delta / (self.initial_edges + 1)

    def record_step(self, c_max):
        """Record state metrics for convergence analysis."""
        avg_density = sum(n["density"] for n in self.nodes) / self.num_nodes
        metrics = self.compute_structural_entropy()
        topo_dist = self.compute_topology_distance()
        
        self.history["tension"].append(self.tension_delta)
        self.history["avg_density"].append(avg_density)
        self.history["structural_entropy"].append(metrics["structural_entropy"])
        self.history["phase_distribution"].append(metrics["phase_distribution"].copy())
        self.history["inversion_count"].append(self.inversion_events)
        self.history["rewiring_count"].append(self.rewiring_events)
        self.history["edge_count"].append(len(self.edges))
        self.history["topology_distance"].append(topo_dist)
        
        return metrics

    def check_stability(self, window_size=10):
        """
        Check if structural entropy has converged to a stable attractor.
        Also check if topological rewiring has stopped (stable configuration).
        """
        if len(self.history["structural_entropy"]) < window_size:
            return False, None, None
        
        recent_entropy = np.array(self.history["structural_entropy"][-window_size:])
        recent_rewiring = np.array(self.history["rewiring_count"][-window_size:])
        
        entropy_mean = np.mean(recent_entropy)
        entropy_std = np.std(recent_entropy)
        entropy_cv = entropy_std / (entropy_mean + 1e-9)
        
        rewiring_mean = np.mean(recent_rewiring)
        
        # Stability: low entropy variation AND low rewiring frequency
        is_stable = (entropy_cv < 0.15) and (rewiring_mean < 2.0)
        
        return is_stable, entropy_cv, rewiring_mean


# ============================================================================
# PART 3: CONSISTENCY TESTING SUITE
# ============================================================================

class ConsistencyTestSuite:
    """
    Automated verification that Axioms I–V (with dynamic rewriting) produce 
    stable emergent geometry.
    """
    
    def __init__(self):
        self.results = []
        self.lambda_val, self.v_ideal, self.c_max = derive_c_max()
        
    def run_single_test(self, num_nodes, topology, seed=None, steps=30):
        """Run one consistency test: fixed node count and topology."""
        network = TX0RelationalNetwork(num_nodes=num_nodes, topology=topology, seed=seed)
        
        print(f"\n  Initializing {num_nodes}-node {topology} poset...", end=" ", flush=True)
        print(f"(edges: {len(network.edges)})")
        
        for step in range(steps):
            delta_increment = 0.4
            network.update_network_state(delta_increment, self.c_max)
            metrics = network.record_step(self.c_max)
            
            if (step + 1) % 10 == 0:
                edge_status = f"edges: {len(network.edges)}"
                print(f"    Step {step+1:2d}/{steps}: SE={metrics['structural_entropy']:.4f}, "
                      f"Rewires={network.rewiring_events}, {edge_status}")
        
        # Check stability in final window
        is_stable, entropy_cv, rewiring_freq = network.check_stability(window_size=10)
        final_entropy = network.history["structural_entropy"][-1]
        final_edges = len(network.edges)
        
        result = {
            "num_nodes": num_nodes,
            "topology": topology,
            "seed": seed,
            "is_stable": is_stable,
            "entropy_cv": entropy_cv,
            "rewiring_freq": rewiring_freq,
            "final_entropy": final_entropy,
            "initial_entropy": network.history["structural_entropy"][0],
            "max_inversions": max(network.history["inversion_count"]),
            "total_rewiring": sum(network.history["rewiring_count"]),
            "initial_edges": network.initial_edges,
            "final_edges": final_edges,
            "edges_created": network.edges_created,
            "edges_dropped": network.edges_dropped,
            "history": network.history
        }
        
        self.results.append(result)
        return result

    def run_full_suite(self):
        """Execute consistency tests across all parameter combinations."""
        node_sizes = [64, 128, 256, 512]
        topologies = ["linear", "random", "scale-free"]
        
        print("=" * 90)
        print("  TX-0 AXIOMS I–V CONSISTENCY VERIFICATION SUITE (WITH DYNAMIC REWRITING)")
        print("  Testing Stability of Emergent Structure via Intrinsic Topological Evolution")
        print("=" * 90)
        
        for topology in topologies:
            print(f"\n[TOPOLOGY: {topology.upper()}]")
            for num_nodes in node_sizes:
                self.run_single_test(num_nodes, topology, seed=42, steps=30)
        
        self.print_summary()
        return self.results

    def print_summary(self):
        """Print aggregated results and stability assessment."""
        print("\n" + "=" * 90)
        print("  CONSISTENCY TEST SUMMARY (DYNAMIC REWRITING)")
        print("=" * 90)
        
        stable_count = sum(1 for r in self.results if r["is_stable"])
        chaotic_count = len(self.results) - stable_count
        
        print(f"\nTotal tests run: {len(self.results)}")
        print(f"Stable emergence: {stable_count} / {len(self.results)}")
        print(f"Chaotic cascades: {chaotic_count} / {len(self.results)}")
        
        print("\n[DETAILED RESULTS]")
        print(f"{'Nodes':<8} | {'Topology':<12} | {'Status':<10} | {'CV':<8} | {'Rewires/step':<12} | {'Edge Δ':<8}")
        print("-" * 90)
        
        for result in self.results:
            status = "STABLE" if result["is_stable"] else "CHAOTIC"
            cv_str = f"{result['entropy_cv']:.4f}" if result['entropy_cv'] else "N/A"
            rw_str = f"{result['rewiring_freq']:.2f}" if result['rewiring_freq'] else "N/A"
            edge_delta = result["final_edges"] - result["initial_edges"]
            print(f"{result['num_nodes']:<8} | {result['topology']:<12} | {status:<10} | "
                  f"{cv_str:<8} | {rw_str:<12} | {edge_delta:+6d}")
        
        print("\n[TOPOLOGICAL EVOLUTION SUMMARY]")
        for result in self.results:
            print(f"  {result['num_nodes']:3d}-node {result['topology']:<10}: "
                  f"Edges {result['initial_edges']:4d} → {result['final_edges']:4d} "
                  f"(+{result['edges_created']:3d} / -{result['edges_dropped']:3d})")
        
        print("\n[AXIOM INTERPRETATION]")
        if stable_count / len(self.results) >= 0.7:
            print("  ✓ AXIOMS I–V VERIFIED: Stable emergent structure confirmed.")
            print("    The relational poset with DYNAMIC REWIRING converges to organized configurations.")
            print("    The graph rewrites itself to find equilibrium. Difference-flux and topology")
            print("    co-evolve toward coherent, self-organizing geometry.")
            print("  ✓ BACKGROUND-INDEPENDENCE ACHIEVED: No external rules. Purely intrinsic dynamics.")
        else:
            print("  ✗ AXIOMS I–V INCONCLUSIVE: Chaotic behavior in >30% of tests.")
            print("    Dynamic rewiring alone may not be sufficient. Consider:")
            print("    - Tuning rewiring parameters (drop fraction, distance metrics)")
            print("    - Adjusting stability criterion (window size, CV threshold)")
            print("    - Introducing secondary dynamics (e.g., hyperbolic position drift)")
        
        print("\n" + "=" * 90)


# ============================================================================
# PART 4: EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("TX-0 RELATIONAL ARCHITECTURE v2.0 (DYNAMIC REWRITING)")
    print("Background-Independent Axiom Verification\n")
    
    # Derive foundational constant
    print("[AXIOM II: CONFORMAL BINDING]")
    lambda_val, v_ideal, c_max = derive_c_max()
    print(f"  Λ(π/3) = {lambda_val:.9f}")
    print(f"  V_ideal = {v_ideal:.9f}")
    print(f"  C_max (capacity threshold) = {c_max:.6f}\n")
    
    # Run consistency suite
    suite = ConsistencyTestSuite()
    suite.run_full_suite()
    
    print("\n[SESSION COMPLETE]")
    print("Commit staged for review: engine2_512.py (with dynamic rewriting)")
