# MSDS 610: AI I: Deep Learning

**Credits:** 3  
**Level:** graduate  
**Prerequisites:** ISA 530

## Course Description
Advanced deep learning concepts and implementation for data science applications.

## Key Topics
- Deep learning
- Neural network architectures
- Training techniques
- GPU computing

---

## Information Bank
*Research and supplementary materials for each key topic below.*

### Deep learning

Deep learning is an advanced subset of machine learning that uses multi-layer neural networks to learn hierarchical representations of data, where the term "deep" refers to the multiple levels or stages through which data is processed. Unlike traditional machine learning, deep learning does not require manual feature engineering because it performs hierarchical feature learning — higher-level features are defined in terms of lower-level features, allowing the model to learn complex mappings from input to output directly from raw data. It is the driving force behind many modern AI breakthroughs in vision, language, and decision-making.

- **Multi-layer architecture**: Deep networks consist of an input layer, multiple hidden layers that progressively refine data representations, and an output layer that produces predictions
- **Automatic feature extraction**: Deep learning eliminates the need for hand-crafted features by learning useful representations directly from data through successive nonlinear transformations
- **Universal approximation**: Sufficiently deep networks can approximate virtually any continuous function, giving them extraordinary modeling flexibility
- **Loss functions and objectives**: Training is driven by minimizing a loss function (e.g., cross-entropy for classification, mean squared error for regression) that quantifies prediction error
- **End-to-end learning**: Entire pipelines — from raw input to final output — can be trained jointly, enabling the network to co-optimize all processing stages
- **Scalability with data**: Deep learning models improve with more data and compute, making them especially powerful in big-data regimes where traditional methods plateau

**Practical Applications:** Deep learning powers image recognition systems in healthcare (e.g., radiology diagnostics), natural language processing applications like machine translation and chatbots, autonomous vehicle perception systems, and recommendation engines used by streaming and e-commerce platforms.

---

### Neural network architectures

Neural network architectures define the structural design of how neurons are organized, connected, and how data flows through a model. The three dominant architecture families in modern deep learning are Convolutional Neural Networks (CNNs) for spatial data, Recurrent Neural Networks (RNNs) for sequential data, and Transformers which use attention mechanisms for parallel processing of sequences. Selecting the right architecture is a critical design decision that depends on the nature of the input data and the task at hand.

- **Convolutional Neural Networks (CNNs)**: Use convolutional filters that slide across input data to detect local patterns (edges, textures, shapes), paired with pooling layers that reduce spatial dimensions while preserving important features; dominant in computer vision tasks
- **Recurrent Neural Networks (RNNs)**: Process sequential data through a feedback loop where the output from one time step feeds into the next, maintaining a hidden state that acts as memory; variants like LSTMs and GRUs address the vanishing gradient problem that affects vanilla RNNs
- **Transformers**: Process all input tokens simultaneously using self-attention mechanisms that determine how each part of the input relates to every other part, enabling massive parallelism and superior performance on long sequences
- **Generative Adversarial Networks (GANs)**: Consist of a generator and discriminator competing in a minimax game, enabling the synthesis of realistic images, audio, and other data
- **Autoencoders and Variational Autoencoders (VAEs)**: Encode input into a compressed latent representation and decode it back, useful for dimensionality reduction, anomaly detection, and generative modeling
- **Graph Neural Networks (GNNs)**: Operate on graph-structured data by passing messages between connected nodes, applicable to social networks, molecular modeling, and knowledge graphs

**Practical Applications:** CNNs drive medical image analysis and facial recognition, RNNs and Transformers power language models and speech recognition systems, and GANs are used in creative AI for generating photorealistic images and data augmentation in low-data scenarios.

---

### Training techniques

Training deep neural networks involves iteratively adjusting model weights to minimize a loss function, primarily through backpropagation and gradient descent. Backpropagation efficiently computes the gradient of the loss with respect to each weight by propagating derivatives backward from the output layer to the input layer, avoiding redundant chain-rule calculations. Effective training requires careful selection of optimization algorithms, regularization strategies, and hyperparameters to ensure the model converges to a good solution without overfitting.

- **Optimization algorithms**: Stochastic Gradient Descent (SGD) and adaptive methods like Adam, RMSprop, and AdaGrad dynamically adjust learning rates based on gradient history, accelerating convergence and navigating complex loss landscapes more effectively
- **Regularization via Dropout**: Randomly deactivates a fraction of neurons during each training step, forcing the network to learn redundant representations and preventing co-adaptation of features; higher dropout rates apply stronger regularization
- **Batch normalization**: Normalizes the inputs to each layer during training, mitigating internal covariate shift, allowing higher learning rates, and significantly speeding up convergence
- **Learning rate scheduling**: Strategies such as step decay, cosine annealing, and warm-up schedules adjust the learning rate over training epochs to balance fast early progress with fine-grained later optimization
- **Early stopping**: Monitors validation performance during training and halts the process when performance begins to degrade, preventing overfitting without requiring explicit regularization parameters
- **Data augmentation**: Applies random transformations (rotations, flips, crops, noise) to training samples to artificially increase dataset diversity, improving generalization especially when labeled data is scarce

**Practical Applications:** These techniques are essential in every deep learning workflow — for example, Adam optimization with dropout and batch normalization forms the standard training recipe for production image classifiers, while learning rate scheduling and early stopping are critical for fine-tuning large pre-trained language models on domain-specific datasets.

---

### GPU computing

GPU computing leverages the massively parallel architecture of Graphics Processing Units to accelerate computationally intensive tasks, particularly deep learning model training and inference. While CPUs excel at executing a few complex sequential threads quickly, GPUs are designed to execute thousands of simpler threads simultaneously, making them ideal for the matrix and tensor operations at the core of neural networks. NVIDIA's CUDA platform, released in 2007, is the dominant programming model that enables developers to harness GPU parallelism for general-purpose computing.

- **CUDA platform**: NVIDIA's parallel computing platform and programming model provides APIs in C++, Python, and Fortran, along with GPU-accelerated libraries (cuDNN for deep learning primitives, cuBLAS for linear algebra) that form the backbone of modern deep learning frameworks
- **Parallelism model**: GPUs decompose problems into thousands of lightweight threads organized into blocks and grids, enabling simultaneous execution of matrix multiplications, convolutions, and element-wise operations that dominate neural network computation
- **Framework integration**: Major deep learning frameworks — PyTorch, TensorFlow, JAX, and MXNet — rely on CUDA for GPU acceleration, abstracting low-level GPU programming so practitioners can focus on model design
- **Training speedups**: GPU acceleration reduces deep learning training times from months to days or hours; multi-GPU and distributed training strategies (data parallelism, model parallelism) scale to even larger models and datasets
- **Memory management**: GPU memory (VRAM) is a key constraint; techniques like mixed-precision training (FP16/BF16), gradient checkpointing, and memory-efficient attention allow training of larger models within limited GPU memory budgets
- **Inference optimization**: NVIDIA TensorRT and similar tools optimize trained models for deployment by fusing layers, quantizing weights, and leveraging GPU-specific optimizations to minimize latency in production

**Practical Applications:** GPU computing is indispensable in modern AI — cloud providers offer GPU instances (NVIDIA A100, H100) for training large language models and diffusion models, while edge GPU devices (Jetson series) enable real-time inference in robotics, autonomous vehicles, and IoT applications.

---

