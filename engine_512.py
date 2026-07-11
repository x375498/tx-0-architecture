"""
TX-0 Engine Array Simulator (Version 2.0.0-Stable)
Core Logic: Causal Poset Routing & Hyperbolic Saturation Bifurcation
"""

import math
import time
import random

# Core Framework Constants (From Step Zero)
NODE_COUNT = 512
C_MAX = 4.5558  # Asymptotic Density Limit (Axiom V)
BASE_DELTA = 0.1337  # Primordial Asymmetry Remainder (Axiom II)

class TX0Node:
    def __init__(self, node_id):
        self.id = node_id
        self.load = BASE_DELTA  # Initialized with non-zero remainder
        self.routing_dimension = 1  # Starts at R_1 (Linear Queue)
        self.connections = []
        self.phase_alignment = random.uniform(0, 2 * math.pi)

    def calculate_local_density(self):
        """
        Simulates local nodal data-density within a bounded hyperbolic neighborhood.
        In a dense graph, the load scales non-linearly with active connections.
        """
        connection_factor = math.log1p(len(self.connections)) if self.connections else 0
        # Density is a function of current load, network connections, and phase resonance
        density = (self.load * (1.0 + connection_factor)) + (0.05 * math.sin(self.phase_alignment))
        return round(density, 4)

    def process_incoming_tension(self, incoming_load):
        self.load += incoming_load
        current_density = self.calculate_local_density()

        # Axiom V Check: Has local density breached the absolute structural ceiling?
        if current_density >= C_MAX:
            self.execute_micro_inversion(current_density)
        # Axiom III Check: Latency queue saturation routing
        elif self.load > 2.5 and self.routing_dimension == 1:
            self.buckle_to_plane()

    def buckle_to_plane(self):
        """Axiom III: Linear trajectory R_1 buckles into R_2 rotational plane."""
        self.routing_dimension = 2
        # Phase shifts orthogonally to handle the load distribution
        self.phase_alignment += math.pi / 2 

    def execute_micro_inversion(self, breached_density):
        """Axiom V & VI: Micro-inversion translating raw tension into physical observables."""
        # Calculate excess tension above structural threshold
        excess = breached_density - C_MAX
        
        # Inversion event: Reset load to baseline and distribute the rest as emergent vectors
        self.load = BASE_DELTA
        self.routing_dimension = 3  # Expands to R_3 Volumetric Frame
        
        # Translate excess network tension into simulated physical properties
        emergent_mass = excess * 1.618  # Scaled by golden ratio
        emergent_charge = math.cos(self.phase_alignment) * 1.0
        
        print(f" [Axiom V/VI Micro-Inversion] Node {self.id:03d} breached C_max ({breached_density} >= {C_MAX})")
        print(f"   ├─ Dimension Expanded: R_{self.routing_dimension}")
        print(f"   └─ Egested Observables -> Mass: {emergent_mass:.4f} | Charge: {emergent_charge:.4f}")

def run_simulation_cycle():
    print("=" * 70)
    print(f"INITIALIZING TX-0 ENGINE ARRAY ({NODE_COUNT} RELATIONAL NODES)")
    print(f"System Baseline Remainder (\u0394): {BASE_DELTA} | Density Threshold (C_max): {C_MAX}")
    print("=" * 70)
    time.sleep(1)

    # Initialize the 512-node Causal Poset
    engine_array = [TX0Node(i) for i in range(NODE_COUNT)]

    # Form random network topologies (Simulating initial relational graph)
    for node in engine_array:
        sample_size = random.randint(2, 6)
        node.connections = random.sample([n.id for n in engine_array if n.id != node.id], sample_size)

    # Step Execution Loop: Pump continuous informational load into the network
    try:
        step = 0
        while True:
            step += 1
            # Inject randomized tension events into the network matrix
            active_nodes = random.sample(engine_array, random.randint(5, 15))
            
            for target_node in active_nodes:
                raw_tension_input = random.uniform(0.5, 1.5)
                target_node.process_incoming_tension(raw_tension_input)

                # Axiom VI Cascade: Distribute load down to neighboring nodes
                for neighbor_id in target_node.connections:
                    cascade_load = raw_tension_input * 0.25  # Dissipation factor
                    engine_array[neighbor_id].process_incoming_tension(cascade_load)

            # System telemetry print every 10 steps
            if step % 10 == 0:
                dimensions = [n.routing_dimension for n in engine_array]
                print(f"[Cycle {step:03d}] Active Dimensions Across Poset -> R1: {dimensions.count(1)} | R2: {dimensions.count(2)} | R3: {dimensions.count(3)}")
                time.sleep(0.5)

    except KeyboardInterrupt:
        print("\n[Engine Paused] Simulation loop broken by user. Baseline network layout preserved.")
        print("=" * 70)

if __name__ == "__main__":
    run_simulation_cycle()
