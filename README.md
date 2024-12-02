# PCI Patterns and Workflows for COAR Notify

Based on the `coarnotify` library

## Adding a pattern refinement

1. Create a new module in pcinotify.patterns and extend the Pattern class as needed
2. Import the class in pcinotify.patterns.__init__
3. Add the class to pcinotify.factory
4. Add tests in test_models and test_factory