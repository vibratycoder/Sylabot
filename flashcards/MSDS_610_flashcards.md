# MSDS 610: AI I: Deep Learning - Flashcard Reference Bank

---

## Deep Learning

### Key Terms & Definitions
- **Deep Learning**: A subset of machine learning that uses multi-layer neural networks to learn hierarchical representations of data without manual feature engineering
- **Neural Network**: A computational model inspired by biological neurons, consisting of interconnected layers of nodes that process and transform input data
- **Hidden Layer**: An intermediate layer between input and output layers where learned representations are progressively refined
- **Loss Function**: A mathematical function that quantifies prediction error (e.g., cross-entropy, mean squared error) and drives the training process
- **Feature Learning**: The automatic extraction of useful data representations through successive nonlinear transformations, eliminating the need for hand-crafted features
- **Universal Approximation Theorem**: The principle that sufficiently deep networks can approximate virtually any continuous function
- **End-to-End Learning**: Training an entire pipeline jointly from raw input to final output, allowing co-optimization of all processing stages
- **Activation Function**: A nonlinear function (e.g., ReLU, sigmoid, tanh) applied to neuron outputs to enable the network to learn complex, nonlinear mappings
- **Epoch**: One complete pass through the entire training dataset during model training
- **Overfitting**: When a model learns noise in training data rather than general patterns, resulting in poor performance on unseen data
- **Underfitting**: When a model is too simple to capture underlying patterns in the data

### Core Concepts (Q&A Format)
- Q: Why is "deep" learning called deep?
- A: Because the models use multiple hidden layers (depth) that progressively refine data representations from simple to complex features.

- Q: What distinguishes deep learning from traditional machine learning?
- A: Deep learning automatically learns hierarchical feature representations from raw data, whereas traditional ML requires manual feature engineering.

- Q: Why do deep learning models improve with more data?
- A: Deep networks have high capacity (many parameters) that can capture subtle patterns only visible in large datasets, while traditional methods plateau due to limited model complexity.

- Q: What role do activation functions play in neural networks?
- A: They introduce nonlinearity, enabling the network to learn complex functions. Without them, stacking layers would only produce a linear transformation.

- Q: What is the difference between cross-entropy and mean squared error loss?
- A: Cross-entropy is used for classification tasks and measures divergence between predicted probability distributions and true labels. MSE is used for regression and measures average squared difference between predicted and actual values.

- Q: What does end-to-end learning mean and why is it valuable?
- A: It means training the entire pipeline (from raw input to output) jointly, allowing all processing stages to co-optimize rather than being designed independently.

- Q: How does the universal approximation theorem relate to deep learning?
- A: It guarantees that neural networks with sufficient depth/width can approximate any continuous function, providing theoretical justification for their modeling power.

### Important Facts & Figures
- Deep learning is the driving force behind modern AI breakthroughs in vision, language, and decision-making
- The term "deep" refers to the multiple levels or stages through which data is processed, not the depth of understanding
- Higher-level features are defined in terms of lower-level features (hierarchical feature learning)
- Deep learning powers: image recognition in healthcare, machine translation, autonomous vehicle perception, and recommendation engines
- A single hidden layer network is a universal approximator in theory, but deeper networks learn more efficiently in practice
- Deep learning performance scales with both data volume and compute power
- The field gained major momentum after 2012 when AlexNet won the ImageNet competition using GPU-accelerated deep learning

### Common Exam Questions
- Q: Explain what hierarchical feature learning is and why it matters in deep learning.
- A: Hierarchical feature learning means that lower layers detect simple patterns (edges, textures) while higher layers combine them into complex representations (faces, objects). This eliminates manual feature engineering and allows the network to discover optimal representations directly from raw data.

- Q: Compare and contrast deep learning with traditional machine learning in terms of data requirements and feature engineering.
- A: Traditional ML requires manual feature engineering and works well with smaller datasets. Deep learning automatically extracts features but requires large datasets and significant compute resources. DL performance continues to improve with more data, while traditional ML tends to plateau.

- Q: What is a loss function and how does it drive training?
- A: A loss function quantifies the error between model predictions and true values. Training minimizes this function by iteratively adjusting weights via gradient descent. Common losses include cross-entropy (classification) and MSE (regression).

- Q: Why are nonlinear activation functions necessary in deep neural networks?
- A: Without nonlinear activations, any combination of linear layers collapses into a single linear transformation, limiting the network to modeling only linear relationships. Nonlinear activations enable learning complex, nonlinear mappings.

---

## Neural Network Architectures

### Key Terms & Definitions
- **Convolutional Neural Network (CNN)**: Architecture using convolutional filters to detect local spatial patterns, dominant in computer vision tasks
- **Recurrent Neural Network (RNN)**: Architecture with feedback loops that maintains a hidden state to process sequential data one step at a time
- **Transformer**: Architecture that uses self-attention mechanisms to process all input tokens simultaneously in parallel
- **LSTM (Long Short-Term Memory)**: An RNN variant with gating mechanisms (forget, input, output gates) that solves the vanishing gradient problem for long sequences
- **GRU (Gated Recurrent Unit)**: A simplified LSTM variant with two gates (reset and update) that offers comparable performance with fewer parameters
- **GAN (Generative Adversarial Network)**: Two-network architecture (generator vs. discriminator) that learns to generate realistic synthetic data through adversarial training
- **Autoencoder**: Network that encodes input into a compressed latent representation and decodes it back, used for dimensionality reduction and anomaly detection
- **VAE (Variational Autoencoder)**: Probabilistic autoencoder that learns a smooth latent space, enabling generative sampling of new data points
- **Graph Neural Network (GNN)**: Architecture that operates on graph-structured data by passing messages between connected nodes
- **Self-Attention**: Mechanism that determines how each part of the input relates to every other part, enabling capture of long-range dependencies
- **Pooling Layer**: A layer that reduces spatial dimensions of feature maps while preserving important features (e.g., max pooling, average pooling)
- **Convolutional Filter/Kernel**: A small learnable weight matrix that slides across input data to detect local patterns

### Core Concepts (Q&A Format)
- Q: What is the key difference between CNNs and RNNs?
- A: CNNs process spatial data using local filters (parameter sharing across spatial locations), while RNNs process sequential data using feedback loops that maintain temporal memory through hidden states.

- Q: How do Transformers differ from RNNs in processing sequences?
- A: Transformers process all tokens simultaneously using self-attention (parallel), while RNNs process tokens one at a time sequentially. This makes Transformers much faster to train and better at capturing long-range dependencies.

- Q: What problem do LSTMs and GRUs solve that vanilla RNNs cannot?
- A: They solve the vanishing gradient problem, which causes vanilla RNNs to lose information from early time steps. LSTMs use forget/input/output gates, while GRUs use reset/update gates to control information flow.

- Q: How does a GAN work?
- A: A generator creates fake data from random noise, while a discriminator tries to distinguish real from fake. They compete in a minimax game, with the generator improving until its outputs are indistinguishable from real data.

- Q: What is the purpose of pooling in CNNs?
- A: Pooling reduces spatial dimensions (downsampling) to decrease computation, provide translation invariance, and prevent overfitting while retaining the most important features.

- Q: Why are GNNs needed when we already have CNNs and RNNs?
- A: CNNs work on grids (images) and RNNs on sequences (text), but many real-world data structures are graphs (social networks, molecules). GNNs can process arbitrary graph topologies by passing messages between connected nodes.

- Q: What advantage do autoencoders provide for anomaly detection?
- A: Autoencoders learn to reconstruct normal data well. Anomalous inputs produce high reconstruction error, making them easy to flag as outliers.

### Important Facts & Figures
- CNNs use three key operations: convolution (feature detection), pooling (downsampling), and fully connected layers (classification)
- The Transformer was introduced in 2017 in the paper "Attention Is All You Need"
- LSTM networks have three gates: forget gate, input gate, and output gate
- GRUs have two gates: reset gate and update gate (simpler than LSTM)
- GANs were introduced by Ian Goodfellow in 2014
- CNNs exploit parameter sharing -- the same filter is applied across the entire input, dramatically reducing parameters vs. fully connected layers
- Transformers enable massive parallelism during training, making them much faster than RNNs for long sequences

### Common Exam Questions
- Q: Compare CNNs, RNNs, and Transformers in terms of their ideal use cases and how they process data.
- A: CNNs: best for spatial data (images), use local filters sliding across input. RNNs: best for sequential data, process one step at a time with hidden state memory. Transformers: best for text/long sequences, use self-attention to process all tokens in parallel. Transformers have largely replaced RNNs for NLP due to superior parallelism and long-range dependency handling.

- Q: Explain the generator-discriminator dynamic in GANs.
- A: The generator produces synthetic data from random noise. The discriminator classifies inputs as real or fake. Through adversarial training, the generator improves at creating realistic data while the discriminator improves at detecting fakes, until equilibrium is reached.

- Q: What is the vanishing gradient problem and how do LSTMs address it?
- A: In vanilla RNNs, gradients shrink exponentially during backpropagation through many time steps, preventing learning of long-range dependencies. LSTMs use gating mechanisms (forget, input, output gates) to maintain a cell state that can carry information across many time steps without gradient degradation.

- Q: Describe the self-attention mechanism and explain why it is central to the Transformer architecture.
- A: Self-attention computes relevance scores between all pairs of tokens in a sequence, producing weighted representations that capture contextual relationships regardless of distance. This enables parallelism (unlike sequential RNNs) and better long-range dependency modeling, forming the core innovation of Transformers.

---

## Training Techniques

### Key Terms & Definitions
- **Backpropagation**: Algorithm that computes gradients of the loss with respect to each weight by propagating derivatives backward from output to input using the chain rule
- **Gradient Descent**: Optimization algorithm that iteratively adjusts weights in the direction that reduces the loss function
- **Stochastic Gradient Descent (SGD)**: Gradient descent variant that updates weights using a random subset (mini-batch) of training data per iteration
- **Adam Optimizer**: Adaptive optimizer that maintains exponential moving averages of past gradients and squared gradients, adjusting learning rates per-parameter
- **Learning Rate**: Hyperparameter that controls the step size of weight updates during optimization
- **Dropout**: Regularization technique that randomly deactivates a fraction of neurons during training to prevent co-adaptation and overfitting
- **Batch Normalization**: Technique that normalizes layer inputs across a mini-batch, reducing internal covariate shift and enabling higher learning rates
- **Early Stopping**: Halting training when validation performance starts to degrade, preventing overfitting without explicit regularization
- **Data Augmentation**: Applying random transformations (rotations, flips, crops) to training samples to increase dataset diversity artificially
- **Learning Rate Scheduling**: Strategies (step decay, cosine annealing, warm-up) that adjust the learning rate during training for optimal convergence
- **Regularization**: Techniques (L1, L2, dropout) that constrain the model to prevent overfitting and improve generalization
- **Mini-Batch**: A small subset of training data used for a single weight update step

### Core Concepts (Q&A Format)
- Q: How does backpropagation work?
- A: It computes the gradient of the loss with respect to each weight by applying the chain rule backward from the output layer to the input layer. The forward pass computes outputs and stores intermediate values; the backward pass uses these to efficiently calculate all gradients.

- Q: What is the difference between SGD and Adam?
- A: SGD uses a fixed learning rate for all parameters and updates based on current gradient. Adam adapts learning rates per-parameter using exponential moving averages of first (mean) and second (variance) moments of gradients, generally converging faster.

- Q: Why does dropout help prevent overfitting?
- A: By randomly deactivating neurons during training, dropout forces the network to learn redundant, distributed representations rather than relying on any single neuron. This creates an implicit ensemble effect, improving generalization.

- Q: What is internal covariate shift and how does batch normalization address it?
- A: Internal covariate shift is the change in the distribution of layer inputs during training as earlier layers update. Batch normalization standardizes inputs to each layer (zero mean, unit variance) per mini-batch, stabilizing training and allowing higher learning rates.

- Q: When should you use early stopping vs. other regularization methods?
- A: Early stopping is simple and effective when you have a clear validation set. It can be combined with other methods (dropout, L2). Use early stopping when you want to avoid tuning regularization hyperparameters -- it automatically finds the optimal training duration.

- Q: What is the recommended order of applying batch normalization and dropout?
- A: The standard sequence is: Linear Transformation -> Batch Normalization -> Activation Function -> Dropout.

- Q: Why is data augmentation important when labeled data is scarce?
- A: It artificially increases the effective size and diversity of the training set by applying random transformations, helping the model generalize better without requiring additional labeled examples.

### Important Facts & Figures
- Adam optimizer combines the benefits of RMSprop and momentum, maintaining per-parameter adaptive learning rates
- Typical dropout rates range from 0.2 to 0.5; higher rates apply stronger regularization
- Batch normalization was introduced by Ioffe and Szegedy in 2015
- Common learning rate schedules: step decay (reduce by factor every N epochs), cosine annealing (smooth decay following cosine curve), warm-up (start small and increase)
- Data augmentation transformations include: rotation, horizontal/vertical flip, random crop, color jitter, Gaussian noise, and mixup
- The standard training recipe for production image classifiers: Adam + dropout + batch normalization
- For fine-tuning pre-trained language models: learning rate scheduling + early stopping are critical

### Common Exam Questions
- Q: Explain the backpropagation algorithm and its relationship to gradient descent.
- A: Backpropagation efficiently computes the gradient of the loss function with respect to every weight in the network using the chain rule. It propagates error derivatives backward from the output layer. Gradient descent then uses these computed gradients to update weights in the direction that minimizes the loss. Together, they form the core training loop of neural networks.

- Q: Compare dropout and batch normalization as regularization techniques.
- A: Dropout randomly deactivates neurons (typically 20-50%) during training, creating an ensemble effect. Batch normalization normalizes layer inputs per mini-batch, primarily improving training stability but also providing mild regularization. They work differently and are often combined: BN before activation, dropout after activation.

- Q: What happens if the learning rate is too high or too low?
- A: Too high: weight updates overshoot minima, causing divergence or oscillation. Too low: convergence is extremely slow, and the model may get stuck in local minima. Learning rate scheduling addresses this by starting with a higher rate for fast progress and gradually reducing it for fine-grained optimization.

- Q: Describe three strategies to combat overfitting in deep learning.
- A: (1) Dropout: randomly deactivates neurons during training. (2) Early stopping: halts training when validation loss increases. (3) Data augmentation: increases effective dataset size through random transformations. Other options include L1/L2 regularization and reducing model complexity.

---

## GPU Computing

### Key Terms & Definitions
- **GPU (Graphics Processing Unit)**: Massively parallel processor designed to execute thousands of threads simultaneously, ideal for matrix and tensor operations in deep learning
- **CUDA (Compute Unified Device Architecture)**: NVIDIA's parallel computing platform and programming model for general-purpose GPU computing, released in 2007
- **CUDA Core**: An individual processing unit within an NVIDIA GPU; modern GPUs contain thousands (e.g., RTX 4090 has 16,384 CUDA cores)
- **VRAM (Video RAM)**: Dedicated high-bandwidth memory on the GPU, a key constraint for model size during training and inference
- **cuDNN**: NVIDIA's GPU-accelerated library of primitives for deep learning, providing optimized implementations of convolutions, pooling, and normalization
- **Mixed-Precision Training**: Using lower-precision formats (FP16/BF16) for computation while maintaining FP32 for critical operations, reducing memory usage and increasing speed
- **Data Parallelism**: Distributing different batches of data across multiple GPUs, each running a copy of the model, and synchronizing gradients
- **Model Parallelism**: Splitting a single large model across multiple GPUs when it cannot fit in one GPU's memory
- **TensorRT**: NVIDIA's inference optimization toolkit that fuses layers, quantizes weights, and applies GPU-specific optimizations for deployment
- **Gradient Checkpointing**: Trading computation for memory by recomputing intermediate activations during backward pass instead of storing them all
- **Tensor Core**: Specialized GPU hardware unit designed for matrix multiply-accumulate operations used in deep learning, available in NVIDIA Volta and later architectures

### Core Concepts (Q&A Format)
- Q: Why are GPUs better than CPUs for deep learning?
- A: GPUs have thousands of cores optimized for parallel execution of simple operations, while CPUs have fewer cores optimized for complex sequential tasks. Deep learning is dominated by matrix multiplications and element-wise operations that benefit enormously from GPU parallelism.

- Q: What is CUDA and why is it important for deep learning?
- A: CUDA is NVIDIA's parallel computing platform that provides APIs and GPU-accelerated libraries enabling developers to harness GPU parallelism. All major deep learning frameworks (PyTorch, TensorFlow, JAX) rely on CUDA for GPU acceleration.

- Q: How does mixed-precision training save memory and compute?
- A: By using FP16 or BF16 instead of FP32 for most operations, memory usage is roughly halved, enabling larger batch sizes or models. Modern Tensor Cores execute FP16 operations much faster than FP32, providing significant speedup with minimal accuracy loss.

- Q: What is the difference between data parallelism and model parallelism?
- A: Data parallelism replicates the entire model on each GPU and distributes different data batches, synchronizing gradients. Model parallelism splits layers of a single model across GPUs, necessary when the model is too large for one GPU's memory.

- Q: Why is VRAM a critical bottleneck in deep learning?
- A: VRAM limits the size of models, batch sizes, and sequence lengths that can be processed. Exceeding VRAM causes out-of-memory errors. Techniques like mixed-precision training, gradient checkpointing, and memory-efficient attention help work within VRAM constraints.

- Q: What does gradient checkpointing trade and why?
- A: It trades computation for memory by discarding intermediate activations during the forward pass and recomputing them during the backward pass. This reduces memory usage significantly (enabling larger models) at the cost of increased training time (~20-30%).

### Important Facts & Figures
- CUDA was released by NVIDIA in 2007
- A typical consumer CPU has ~16 cores; an NVIDIA RTX 4090 has 16,384 CUDA cores; an H100 has 18,432 CUDA cores
- GPU acceleration reduces training times from months to days or hours
- Major frameworks relying on CUDA: PyTorch, TensorFlow, JAX, MXNet
- NVIDIA A100 and H100 are the dominant GPUs for training large AI models in cloud environments
- NVIDIA Jetson series provides edge GPU computing for robotics, autonomous vehicles, and IoT
- cuBLAS handles linear algebra operations; cuDNN handles deep learning primitives on GPU
- The CUDA programming model organizes threads into blocks and grids for parallel execution

### Common Exam Questions
- Q: Compare CPUs and GPUs in terms of architecture and suitability for deep learning workloads.
- A: CPUs have few powerful cores (4-16) optimized for complex sequential operations with large caches. GPUs have thousands of simpler cores (16,000+) designed for massive parallelism. Deep learning involves matrix multiplications and element-wise operations that decompose naturally into thousands of parallel threads, making GPUs orders of magnitude faster for these workloads.

- Q: Explain how CUDA enables deep learning frameworks to leverage GPU hardware.
- A: CUDA provides a programming model (threads organized into blocks and grids) and GPU-accelerated libraries (cuDNN for DL primitives, cuBLAS for linear algebra). Frameworks like PyTorch and TensorFlow build on these abstractions, automatically translating high-level operations into optimized GPU kernels without requiring users to write GPU code directly.

- Q: Describe two techniques for training models that do not fit in a single GPU's memory.
- A: (1) Model parallelism: split the model across multiple GPUs, each holding a portion of the layers. (2) Mixed-precision training: use FP16/BF16 to roughly halve memory consumption. Additional techniques include gradient checkpointing (recompute activations instead of storing them) and memory-efficient attention implementations.

- Q: What is TensorRT and why is it used for inference rather than training?
- A: TensorRT is NVIDIA's inference optimization toolkit that fuses layers, quantizes weights, and applies GPU-specific optimizations to minimize latency. It is designed for deployment rather than training because inference requires fixed model architecture (no gradient computation) and prioritizes low latency and high throughput over flexibility.

---
