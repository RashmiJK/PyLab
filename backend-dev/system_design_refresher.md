## System Design Refresher
- Scalability
- Maintainability
- Efficiency
- Reliability
- Fault tolerance

- Consistency
- Availability
- Partition Tolerance

### CAP theorem
- **Consistency** : It ensures that all nodes in the distributed system have the same data at the same time. This means that if a change is made to one node, that change should be reflected across all other nodes immediately
- **Availability** : Availability ensures that the system is always operational and can respond to requests. This means that even if some nodes are down, the system as a whole should still be able to process requests.
Service Level Objectives (SLOs):
    * SLOs are like setting goals for our system's performance and availability. For example, an SLO might state that a web service should respond to requests within 300 milliseconds and 99.9% of the time
    * Service Level Agreements (SLAs), on the other hand, are formal contracts with our users or customers. They define the minimum level of service we are committing to provide
- **Partition Tolerance** : partition tolerance refers to a distributed system's ability to continue functioning even when a network partition occurs. This means that the system can still operate even if there is a disruption in communication between its nodes.

### Reliability, Fault Tolerance, and Redundancy
- **Reliability** : This means ensuring that our system works correctly and consistently. It's about the system performing as expected, without errors, over time.
- **Fault Tolerance** : This is about preparing for when things go wrong. It defines how our system handles unexpected failures or attacks. Building a fault-tolerant system means it can continue operating even when components fail.
- **Redundancy** : This is about having backups, ensuring that if one part of our system fails, there is another ready to take its place. Implementing redundant systems is a strategy to ensure there's always a backup available in case of failure.