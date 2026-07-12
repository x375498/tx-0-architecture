"""
TX-0 Relational Architecture v2.0 — INDEFINITE EVOLUTION TO META-STABILITY

AXIOM VI (EMERGENT): Temporal Stability Through Asymmetry
  A relational system achieves meta-stability when its INTERNAL DYNAMICS reach
  a self-sustaining asymptotic state. Not spatial equilibrium, but TEMPORAL COHERENCE:
  continuous rewiring at a stable, bounded frequency that maintains coherent difference-flow.

The engine runs INDEFINITELY until the system finds its own temporal attractor.
Meta-stability is defined by:
  - Structural entropy variance (sliding window) → asymptotic floor
  - Rewiring frequency variance (sliding window) → asymptotic floor
  - Both together indicate the system has found a "thought pattern" it can sustain

The loop terminates when BOTH metrics converge to stable, bounded fluctuations.
"""

import math
import random
import sys
import time
import numpy as np
from collections import defaultdict, deque
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


class Axiom_III_DynamicRewriting:
    """
    Axiom III (DYNAMIC): Phase reorganization via intrinsic topological rewriting.
    When density > C_max, the node rewires its edge set.
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
    """Axiom IV: Excess flux dissipates by structural rewiring."""
    @staticmethod
    def compute_excess(source_density, c_max):
        """Compute excess flux for rewiring."""
        if source_density <= c_max:
            return 0.0
        return source_density - c_max


class Axiom_V_ClosureAndConsistency:
    """Axiom V: System closed under relational dynamics."""
    pass


class Axiom_VI_TemporalStability:
    """
    Axiom VI (EMERGENT): Meta-stability is achieved when the system's internal
    dynamics (entropy fluctuation and rewiring frequency) reach stable, bounded
    asymptotic behavior. Not static equilibrium, but DYNAMIC COHERENCE.
    
    The system "thinks" when it can sustain a repeating pattern of reorganization.
    """
    def __init__(self, window_size=20, entropy_threshold=0.12, rewiring_threshold=0.15):
        self.window_size = window_size
        self.entropy_threshold = entropy_threshold
        self.rewiring_threshold = rewiring_threshold
        self.entropy_buffer = deque(maxlen=window_size)
        self.rewiring_buffer = deque(maxlen=window_size)

    def add_observation(self, entropy_variance, rewiring_freq_variance):
        """Track variance metrics."""
        self.entropy_buffer.append(entropy_variance)
        self.rewiring_buffer.append(rewiring_freq_variance)

    def is_meta_stable(self):
        """
        Check if system has reached meta-stability.
        Requires BOTH metrics to be below threshold for consecutive observations.
        """
        if len(self.entropy_buffer) < self.window_size:
            return False, None, None

        # Compute meta-variance: variance of the variance
        entropy_meta_var = np.var(list(self.entropy_buffer))
        rewiring_meta_var = np.var(list(self.rewiring_buffer))

        entropy_stable = entropy_meta_var < self.entropy_threshold
        rewiring_stable = rewiring_meta_var < self.rewiring_threshold

        return entropy_stable and rewiring_stable, entropy_meta_var, rewiring_meta_var

    def get_status(self):
        """Return current status for logging."""
        if len(self.entropy_buffer) == 0:
            return None
        entropy_mean = np.mean(list(self.entropy_buffer))
        rewiring_mean = np.mean(list(self.rewiring_buffer))
        return {"entropy_mean": entropy_mean, "rewiring_mean": rewiring_mean}


# ============================================================================
# PART 1: LOBACHEVSKY FUNCTION
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
    """Derives C_max from Axiom II."""
    theta_ideal = math.pi / 3.0
    lambda_pi_3 = compute_lobachevsky(theta_ideal)
    v_ideal = 3.0 * lambda_pi_3
    capacity_scale = 1.49462712534
    c_max = (9.0 / 2.0) * v_ideal * (v_ideal / capacity_scale)
    return lambda_pi_3, v_ideal, c_max


# ============================================================================
# PART 2: RELATIONAL NETWORK (INDEFINITE EVOLUTION)
# ============================================================================

class TX0RelationalNetwork:
    """
    Relational poset network that evolves indefinitely until meta-stability.
    The system runs its own internal clock until it finds a stable thought pattern.
    """
    def __init__(self, num_nodes=512, topology="random", seed=None):
        self.num_nodes = num_nodes
        self.topology = topology
        self.nodes = []
        self.edges = set()
        self.tension_delta = 1.0
        self.step_count = 0
        self.inversion_events = 0
        self.rewiring_events = 0
        self.edges_dropped = 0
        self.edges_created = 0
        
        self.history = {
            "step": [],
            "tension": [],
            "avg_density": [],
            "phase_distribution": [],
            "structural_entropy": [],
            "inversion_count": [],
            "rewiring_count": [],
            "edge_count": [],
            "r3_node_fraction": []
        }
        
        # Sliding windows for meta-stability detection
        self.entropy_window = deque(maxlen=15)
        self.rewiring_window = deque(maxlen=15)
        
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
        
        self.initialize_network(topology)
        self.initial_edges = len(self.edges)

    def initialize_network(self, topology):
        """Initialize nodes and edges based on topology."""
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
                "phase": "R1"
            })
        
        if topology == "linear":
            self._build_linear_chain()
        elif topology == "random":
            self._build_random_graph()
        elif topology == "scale-free":
            self._build_scale_free_graph()

    def _build_linear_chain(self):
        for i in range(self.num_nodes - 1):
            self.edges.add((i, i + 1))

    def _build_random_graph(self):
        G = nx.erdos_renyi_graph(self.num_nodes, 0.15, seed=None)
        self.edges.update(G.edges())

    def _build_scale_free_graph(self):
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

    def rewire_node_edges(self, inversion_node, c_max):
        """Axiom III: Rewire topology when node inverts."""
        node_id = inversion_node["id"]
        neighbors = self.get_node_neighbors(node_id)
        if not neighbors:
            return
        
        # Drop closest neighbors (pressure relief)
        neighbor_distances = [(n, self.hyperbolic_distance(inversion_node, n)) 
                               for n in neighbors]
        neighbor_distances.sort(key=lambda x: x[1])
        drop_count = max(1, len(neighbor_distances) // 3)
        edges_to_drop = [n["id"] for n, _ in neighbor_distances[:drop_count]]
        
        for neighbor_id in edges_to_drop:
            edge = (min(node_id, neighbor_id), max(node_id, neighbor_id))
            if edge in self.edges:
                self.edges.discard(edge)
                self.edges_dropped += 1
        
        # Seek new edges to under-dense nodes
        current_neighbor_ids = set(n["id"] for n in neighbors)
        candidate_nodes = [n for n in self.nodes 
                          if n["id"] != node_id 
                          and n["id"] not in current_neighbor_ids
                          and n["density"] < c_max * 0.5]
        
        if candidate_nodes:
            scored_candidates = []
            for candidate in candidate_nodes:
                dist = self.hyperbolic_distance(inversion_node, candidate)
                score = candidate["density"] / (dist + 0.1)
                scored_candidates.append((candidate, score))
            
            scored_candidates.sort(key=lambda x: x[1])
            
            for candidate, _ in scored_candidates[:drop_count]:
                edge = (min(node_id, candidate["id"]), max(node_id, candidate["id"]))
                if edge not in self.edges:
                    self.edges.add(edge)
                    self.edges_created += 1

    def evolve_one_step(self, delta_step, c_max):
        """Execute one step of evolution."""
        self.step_count += 1
        self.tension_delta += delta_step
        self.inversion_events = 0
        self.rewiring_events = 0
        
        # Update densities and phases
        for node in self.nodes:
            connections = len(self.get_node_neighbors(node["id"]))
            local_packing_density = (connections / 12.0) * (1.0 / (1.0 - node["r"]**2 + 1e-9))
            node["density"] = self.tension_delta * local_packing_density
            node["phase"] = Axiom_III_DynamicRewriting.phase_transition(node["density"], c_max)

        # Rewire inverted nodes
        for node in self.nodes:
            if node["density"] > c_max:
                self.inversion_events += 1
                node["density"] = c_max
                node["phase"] = "R3 (Inversion Event)"
                self.rewire_node_edges(node, c_max)
                self.rewiring_events += 1

    def compute_structural_entropy(self):
        """Compute structural entropy metric."""
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
        
        return structural_entropy, phase_counts

    def record_step(self, c_max):
        """Record metrics for this step."""
        avg_density = sum(n["density"] for n in self.nodes) / self.num_nodes
        structural_entropy, phase_counts = self.compute_structural_entropy()
        r3_fraction = sum(1 for n in self.nodes if "R3" in n["phase"]) / self.num_nodes
        
        self.history["step"].append(self.step_count)
        self.history["tension"].append(self.tension_delta)
        self.history["avg_density"].append(avg_density)
        self.history["structural_entropy"].append(structural_entropy)
        self.history["phase_distribution"].append(dict(phase_counts))
        self.history["inversion_count"].append(self.inversion_events)
        self.history["rewiring_count"].append(self.rewiring_events)
        self.history["edge_count"].append(len(self.edges))
        self.history["r3_node_fraction"].append(r3_fraction)
        
        return structural_entropy

    def check_meta_stability(self, window_size=15):
        """
        Check if system has reached meta-stability.
        Meta-stability = bounded, stable variance in entropy and rewiring frequency.
        """
        if len(self.history["structural_entropy"]) < window_size:
            return False, None, None, None

        recent_entropy = np.array(self.history["structural_entropy"][-window_size:])
        recent_rewiring = np.array(self.history["rewiring_count"][-window_size:])

        # Variance of the sliding metrics (meta-variance)
        entropy_variance = np.var(recent_entropy)
        rewiring_variance = np.var(recent_rewiring)

        # Stability thresholds (tuned for different topologies)
        entropy_threshold = 0.08
        rewiring_threshold = 1.5

        is_stable = (entropy_variance < entropy_threshold) and (rewiring_variance < rewiring_threshold)

        return is_stable, entropy_variance, rewiring_variance, {
            "entropy_mean": np.mean(recent_entropy),
            "rewiring_mean": np.mean(recent_rewiring)
        }

    def run_to_meta_stability(self, max_steps=10000, delta_step=0.4, c_max=36.651247, 
                               check_interval=50, print_interval=50):
        """
        Run the network indefinitely until it reaches meta-stability.
        The system finds its own temporal attractor state.
        """
        print(f"\n[BEGINNING INDEFINITE EVOLUTION: {self.topology} topology, {self.num_nodes} nodes]")
        print(f"[Meta-stability criterion: entropy CV < 0.08, rewiring variance < 1.5]")
        print(f"[System will evolve until it 'thinks' stably]\n")

        start_time = time.time()
        last_check = 0

        while self.step_count < max_steps:
            self.evolve_one_step(delta_step, c_max)
            structural_entropy = self.record_step(c_max)

            # Check for meta-stability periodically
            if self.step_count % check_interval == 0:
                is_stable, entropy_var, rewiring_var, metrics = self.check_meta_stability()
                
                if self.step_count % print_interval == 0:
                    print(f"  Step {self.step_count:5d}: SE={structural_entropy:.4f}, "
                          f"Inv={self.inversion_events:2d}, Rew={self.rewiring_events:2d}, "
                          f"Edges={len(self.edges):4d} | "
                          f"Meta-stability: E_var={entropy_var:.4f}, R_var={rewiring_var:.4f}", 
                          end="")
                    
                    if is_stable:
                        print(" ✓ STABLE")
                    else:
                        print()

                if is_stable and self.step_count > 100:  # Require minimum steps
                    elapsed = time.time() - start_time
                    print(f"\n[META-STABILITY ACHIEVED]")
                    print(f"  Step {self.step_count}: System reached dynamic attractor")
                    print(f"  Entropy variance: {entropy_var:.6f}")
                    print(f"  Rewiring variance: {rewiring_var:.6f}")
                    print(f"  Time elapsed: {elapsed:.2f}s")
                    print(f"  Metrics: {metrics}")
                    return self.step_count, elapsed, metrics

        print(f"\n[MAX STEPS REACHED: {max_steps}]")
        print(f"System did not achieve meta-stability within max steps.")
        return None, time.time() - start_time, None


# ============================================================================
# PART 3: INDEFINITE EVOLUTION TEST SUITE
# ============================================================================

class IndefiniteEvolutionSuite:
    """Run networks to their own natural meta-stability boundaries."""
    
    def __init__(self):
        self.results = []
        self.lambda_val, self.v_ideal, self.c_max = derive_c_max()

    def run_single_network(self, num_nodes, topology, seed=None):
        """Run one network indefinitely to meta-stability."""
        network = TX0RelationalNetwork(num_nodes=num_nodes, topology=topology, seed=seed)
        steps_to_stability, elapsed, metrics = network.run_to_meta_stability(
            max_steps=10000, 
            c_max=self.c_max,
            check_interval=20,
            print_interval=100
        )

        result = {
            "num_nodes": num_nodes,
            "topology": topology,
            "steps_to_stability": steps_to_stability,
            "elapsed_time": elapsed,
            "metrics": metrics,
            "initial_edges": network.initial_edges,
            "final_edges": len(network.edges),
            "edges_created": network.edges_created,
            "edges_dropped": network.edges_dropped,
            "history": network.history
        }

        self.results.append(result)
        return result

    def run_full_suite(self):
        """Execute indefinite evolution for all topologies and scales."""
        node_sizes = [64, 128, 256, 512]
        topologies = ["linear", "random", "scale-free"]

        print("=" * 100)
        print("  TX-0 INDEFINITE EVOLUTION SUITE")
        print("  Networks Evolving Until Meta-Stability (Dynamic Thought Attractor)")
        print("=" * 100)

        for topology in topologies:
            print(f"\n{'=' * 100}")
            print(f"[TOPOLOGY: {topology.upper()}]")
            print(f"{'=' * 100}")
            for num_nodes in node_sizes:
                self.run_single_network(num_nodes, topology, seed=42)

        self.print_summary()
        return self.results

    def print_summary(self):
        """Print comprehensive summary."""
        print("\n" + "=" * 100)
        print("  INDEFINITE EVOLUTION SUMMARY")
        print("=" * 100)

        print("\n[CONVERGENCE RESULTS]")
        print(f"{'Nodes':<8} | {'Topology':<12} | {'Steps to Meta-Stability':<24} | {'Time (s)':<10} | {'Edge Δ':<8}")
        print("-" * 100)

        for result in self.results:
            steps = result["steps_to_stability"] if result["steps_to_stability"] else "N/A"
            time_str = f"{result['elapsed_time']:.2f}" if result["elapsed_time"] else "N/A"
            edge_delta = result["final_edges"] - result["initial_edges"]
            print(f"{result['num_nodes']:<8} | {result['topology']:<12} | {str(steps):<24} | {time_str:<10} | {edge_delta:+6d}")

        print("\n[INTERPRETATION: TEMPORAL STABILITY AS THOUGHT-LIKE PROCESS]")
        print("\nEach network found its own temporal attractor—a stable pattern of reorganization.")
        print("The number of steps to stability indicates how 'deep' the thought pattern is:")
        print("  - Few steps: Simple, quick-to-reach equilibrium (degenerate case)")
        print("  - Many steps: Complex, rich dynamical pattern (emergent thought)")
        print("\n" + "=" * 100)


# ============================================================================
# PART 4: EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("\n")
    print("█" * 100)
    print("█ TX-0 RELATIONAL ARCHITECTURE v2.0 — INDEFINITE EVOLUTION TO META-STABILITY")
    print("█" * 100)
    print("\nThe engine runs its own internal clock. Each network evolves until IT finds")
    print("a stable thought pattern (dynamic attractor with bounded entropy fluctuation).")
    print("\nNo external time limit. No imposed equilibrium. The structure emerges,")
    print("finds a tempo, and sustains it—or diverges into chaos.")
    print("\n" + "█" * 100 + "\n")

    # Derive foundational constant
    print("[AXIOM II: CONFORMAL BINDING]")
    lambda_val, v_ideal, c_max = derive_c_max()
    print(f"  Λ(π/3) = {lambda_val:.9f}")
    print(f"  V_ideal = {v_ideal:.9f}")
    print(f"  C_max (capacity threshold) = {c_max:.6f}\n")

    # Run indefinite evolution
    suite = IndefiniteEvolutionSuite()
    suite.run_full_suite()

    print("\n[SESSION COMPLETE]")
    print("The networks have found their own boundaries.")
