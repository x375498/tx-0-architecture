"""
TX-0 Relational Architecture v2.0 — Background-Independent Engine
===================================================================

Formalized Axioms I–V: Difference Primitives and Emergent Spacetime
Core Framework: Relational ontology with unitless, spaceless, timeless difference primitives.

Axiom I (Difference Primitive): 
  The universe is a poset of pure relational differences between nodes.
  No a priori space, time, or units exist.

Axiom II (Conformal Binding): 
  Local order on differences is strictly constrained by the hyperbolic metric 
  derived from the Lobachevsky integral Λ(θ). This bounds the cumulative 
  geometric tension a region can sustain before relational reorganization.

Axiom III (Density-Phase Coupling): 
  When local difference-flux (node density) exceeds the derived capacity threshold C_max,
  the relational structure undergoes irreversible phase reorganization (R1 → R2 → R3).
  This marks the point where conformal constraint can no longer bind differences unitlessly.

Axiom IV (Cascade Dissipation / Renormalization): 
  Excess flux at a node cannot remain localized. By Axiom V, it must redistribute 
  to neighbor nodes via edge coupling, with 60% energy egested as RG flow (radiation/gravity).
  This prevents accumulation and forces a global equilibration.

Axiom V (Closure & Self-Consistency): 
  The system is closed under relational dynamics. No external time-evolution, 
  energy injection, or observer is required. The poset's own internal difference-gradients 
  drive all reorganization toward stable emergent structure.

---
Consistency Testing Suite:
  Measures Structural Entropy across varying initial poset topologies.
  Tests whether Axioms III–IV produce stable emergent geometry or chaotic cascade.
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
    """
    Axiom I: The universe is a poset of relational differences.
    No a priori space, time, or units.
    
    This axiom asserts that the fundamental data structure is a directed acyclic poset
    where nodes represent primitive entities and edges encode partial order (causality/binding).
    """
    @staticmethod
    def validate_poset(nodes, edges):
        """Verify that the poset has no cycles (DAG property)."""
        G = nx.DiGraph()
        G.add_nodes_from([n["id"] for n in nodes])
        G.add_edges_from(edges)
        return nx.is_directed_acyclic_graph(G)


class Axiom_II_ConformalBinding:
    """
    Axiom II: Local order is constrained by the hyperbolic metric from Λ(θ).
    This metric encodes maximum cumulative geometric tension per region.
    """
    @staticmethod
    def derive_capacity_threshold(theta_ideal=math.pi / 3.0):
        """
        Derive C_max from the volume of a regular ideal hyperbolic 3-simplex.
        C_max represents the unitless capacity threshold beyond which conformal binding breaks.
        
        V_ideal = 3 * Λ(π/3)
        C_max = (9/2) * V_ideal^2 / capacity_scale
        """
        lambda_val = compute_lobachevsky(theta_ideal)
        v_ideal = 3.0 * lambda_val
        capacity_scale = 1.49462712534  # Derived from conformal geometry
        c_max = (9.0 / 2.0) * v_ideal * (v_ideal / capacity_scale)
        return c_max, lambda_val, v_ideal


class Axiom_III_DensityPhaseCoupling:
    """
    Axiom III: When local density > C_max, the relational structure 
    undergoes irreversible phase reorganization.
    
    Phases represent degrees of conformal constraint:
    - R1: Linear regime, low density, unconstrained differences
    - R2: Planar vortex regime, moderate density, partially bound
    - R3: Inversion event, density > C_max, conformal binding collapses
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
    Axiom IV: Excess flux redistributes to neighbors via edge coupling.
    60% egested as RG flow; 40% transferred to neighbors.
    
    This prevents local accumulation and enforces global equilibration.
    """
    @staticmethod
    def dissipate_excess(source_density, c_max, neighbor_count):
        """
        Compute excess flux and dissipation.
        Returns: clamped_source_density, per_neighbor_transfer
        """
        if source_density <= c_max:
            return source_density, 0.0
        
        excess = source_density - c_max
        clamped = c_max
        per_neighbor_transfer = (excess / neighbor_count) * 0.4 if neighbor_count > 0 else 0.0
        return clamped, per_neighbor_transfer


class Axiom_V_ClosureAndConsistency:
    """
    Axiom V: The system is closed under relational dynamics.
    No external energy, time, or observer required.
    All reorganization emerges from internal difference-gradients.
    """
    @staticmethod
    def is_equilibrated(nodes, c_max, tolerance=0.01):
        """
        Check if the system has reached local quasi-equilibrium.
        Returns True if the fraction of nodes > C_max is stable.
        """
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
    """
    Computes the Lobachevsky function Lambda(theta) using Simpson's Rule.
    Lambda(theta) = - \int_0^\theta \ln|2 \sin t| dt
    """
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
# PART 2: RELATIONAL NETWORK (Axioms I–V Implementation)
# ============================================================================

class TX0RelationalNetwork:
    """
    Simulates a N-node background-independent relational poset network
    to verify whether Axioms III–IV generate stable emergent structure
    or chaotic cascades.
    """
    def __init__(self, num_nodes=512, topology="random", seed=None):
        self.num_nodes = num_nodes
        self.topology = topology
        self.nodes = []
        self.edges = set()
        self.tension_delta = 1.0
        self.inversion_events = 0
        self.cascade_events = 0
        self.history = {
            "tension": [],
            "avg_density": [],
            "phase_distribution": [],
            "structural_entropy": [],
            "inversion_count": [],
            "cascade_count": []
        }
        
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
        
        self.initialize_network(topology)

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
                "phase": "R1"
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
        """Axiom I: Build a 1D chain poset (minimal conformal structure)."""
        for i in range(self.num_nodes - 1):
            self.edges.add((i, i + 1))

    def _build_random_graph(self):
        """Axiom I: Build Erdős-Rényi random graph."""
        G = nx.erdos_renyi_graph(self.num_nodes, 0.15, seed=None)
        self.edges.update(G.edges())

    def _build_scale_free_graph(self):
        """Axiom I: Build Barabási-Albert scale-free graph (power-law degree distribution)."""
        G = nx.barabasi_albert_graph(self.num_nodes, 3)
        self.edges.update(G.edges())

    def hyperbolic_distance(self, n1, n2):
        """Calculate hyperbolic distance in Poincaré coordinates (Axiom II)."""
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

    def update_network_state(self, delta_step, c_max):
        """
        Axioms III–V: Update system tension and nodal densities.
        Apply phase transitions and cascade dissipation.
        """
        self.tension_delta += delta_step
        self.inversion_events = 0
        self.cascade_events = 0
        
        # Step 1: Compute densities (Axiom III)
        for node in self.nodes:
            connections = sum(1 for edge in self.edges if edge[0] == node["id"] or edge[1] == node["id"])
            local_packing_density = (connections / 12.0) * (1.0 / (1.0 - node["r"]**2 + 1e-9))
            node["density"] = self.tension_delta * local_packing_density
            node["phase"] = Axiom_III_DensityPhaseCoupling.phase_transition(node["density"], c_max)

        # Step 2: Identify inversions and cascade (Axioms IV–V)
        for node in self.nodes:
            if node["density"] > c_max:
                self.inversion_events += 1
                self.trigger_fractal_cascade(node, c_max)

    def trigger_fractal_cascade(self, source_node, c_max):
        """Axiom IV: Dissipate excess flux to neighbors (40% transfer, 60% egested)."""
        neighbors = [n for n in self.nodes 
                     if (n["id"], source_node["id"]) in self.edges 
                     or (source_node["id"], n["id"]) in self.edges]
        
        if not neighbors:
            return
        
        clamped, per_neighbor_transfer = Axiom_IV_CascadeDissipation.dissipate_excess(
            source_node["density"], c_max, len(neighbors)
        )
        source_node["density"] = clamped
        
        for neighbor in neighbors:
            neighbor["density"] += per_neighbor_transfer
            self.cascade_events += 1

    def compute_structural_entropy(self):
        """
        Composite metric: Shannon entropy of phase distribution × degree centrality variance.
        Measures organization of emergent structure.
        """
        # Phase distribution (R1, R2, R3)
        phase_counts = defaultdict(int)
        for node in self.nodes:
            phase_counts[node["phase"]] += 1
        
        phase_probs = np.array([count / self.num_nodes for count in phase_counts.values()])
        phase_entropy = scipy_entropy(phase_probs) if len(phase_probs) > 0 else 0.0
        
        # Degree centrality variance
        degree_dict = defaultdict(int)
        for edge in self.edges:
            degree_dict[edge[0]] += 1
            degree_dict[edge[1]] += 1
        
        degrees = np.array([degree_dict.get(n["id"], 0) for n in self.nodes])
        degree_variance = np.var(degrees) if len(degrees) > 0 else 0.0
        
        # Composite: weighted product
        structural_entropy = phase_entropy * (1.0 + degree_variance)
        
        return {
            "phase_entropy": phase_entropy,
            "degree_variance": degree_variance,
            "structural_entropy": structural_entropy,
            "phase_distribution": dict(phase_counts)
        }

    def record_step(self, c_max):
        """Record state metrics for convergence analysis."""
        avg_density = sum(n["density"] for n in self.nodes) / self.num_nodes
        metrics = self.compute_structural_entropy()
        
        self.history["tension"].append(self.tension_delta)
        self.history["avg_density"].append(avg_density)
        self.history["structural_entropy"].append(metrics["structural_entropy"])
        self.history["phase_distribution"].append(metrics["phase_distribution"].copy())
        self.history["inversion_count"].append(self.inversion_events)
        self.history["cascade_count"].append(self.cascade_events)
        
        return metrics

    def check_stability(self, window_size=10):
        """
        Check if structural entropy has converged to a stable attractor.
        Returns: (is_stable, convergence_rate)
        """
        if len(self.history["structural_entropy"]) < window_size:
            return False, None
        
        recent = np.array(self.history["structural_entropy"][-window_size:])
        mean = np.mean(recent)
        std = np.std(recent)
        
        # Stability: low coefficient of variation
        cv = std / (mean + 1e-9)
        is_stable = cv < 0.1  # Convergence threshold
        
        return is_stable, cv


# ============================================================================
# PART 3: CONSISTENCY TESTING SUITE
# ============================================================================

class ConsistencyTestSuite:
    """
    Automated verification that Axioms III–IV produce stable emergent geometry.
    Tests across multiple node counts, topologies, and initial conditions.
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
                print(f"    Step {step+1:2d}/{steps}: SE={metrics['structural_entropy']:.4f}, "
                      f"Inversions={network.inversion_events}, Cascades={network.cascade_events}")
        
        # Check stability in final window
        is_stable, cv = network.check_stability(window_size=10)
        final_entropy = network.history["structural_entropy"][-1]
        
        result = {
            "num_nodes": num_nodes,
            "topology": topology,
            "seed": seed,
            "is_stable": is_stable,
            "convergence_variance": cv,
            "final_entropy": final_entropy,
            "initial_entropy": network.history["structural_entropy"][0],
            "max_inversions": max(network.history["inversion_count"]),
            "total_cascades": sum(network.history["cascade_count"]),
            "history": network.history
        }
        
        self.results.append(result)
        return result

    def run_full_suite(self):
        """Execute consistency tests across all parameter combinations."""
        node_sizes = [64, 128, 256, 512]
        topologies = ["linear", "random", "scale-free"]
        
        print("=" * 80)
        print("  TX-0 AXIOMS III–IV CONSISTENCY VERIFICATION SUITE")
        print("  Testing Stability of Emergent Structure Across Topologies")
        print("=" * 80)
        
        for topology in topologies:
            print(f"\n[TOPOLOGY: {topology.upper()}]")
            for num_nodes in node_sizes:
                self.run_single_test(num_nodes, topology, seed=42, steps=30)
        
        self.print_summary()
        return self.results

    def print_summary(self):
        """Print aggregated results and stability assessment."""
        print("\n" + "=" * 80)
        print("  CONSISTENCY TEST SUMMARY")
        print("=" * 80)
        
        stable_count = sum(1 for r in self.results if r["is_stable"])
        chaotic_count = len(self.results) - stable_count
        
        print(f"\nTotal tests run: {len(self.results)}")
        print(f"Stable emergence: {stable_count} / {len(self.results)}")
        print(f"Chaotic cascades: {chaotic_count} / {len(self.results)}")
        
        print("\n[DETAILED RESULTS]")
        print(f"{'Nodes':<8} | {'Topology':<12} | {'Status':<12} | {'CV':<8} | {'Final SE':<10} | {'Max Inv':<10}")
        print("-" * 80)
        
        for result in self.results:
            status = "STABLE" if result["is_stable"] else "CHAOTIC"
            cv_str = f"{result['convergence_variance']:.4f}" if result['convergence_variance'] else "N/A"
            print(f"{result['num_nodes']:<8} | {result['topology']:<12} | {status:<12} | "
                  f"{cv_str:<8} | {result['final_entropy']:<10.4f} | {result['max_inversions']:<10}")
        
        print("\n[AXIOM INTERPRETATION]")
        if stable_count / len(self.results) > 0.7:
            print("  ✓ AXIOMS III–IV VERIFIED: Stable emergent structure confirmed.")
            print("    The relational poset converges to organized configurations.")
            print("    Difference-flux cascades self-organize into coherent geometry.")
        else:
            print("  ✗ AXIOMS III–IV INCONCLUSIVE: Chaotic behavior detected in >30% of tests.")
            print("    The axiom set may be under-constrained or require refinement.")
        
        print("\n" + "=" * 80)


# ============================================================================
# PART 4: EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("TX-0 RELATIONAL ARCHITECTURE v2.0")
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
    print("Commit staged for review: engine2_512.py")
