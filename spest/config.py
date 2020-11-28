"""Handles the configuration of this algorithm.

"""
from singleton_config import Config as Config_


class Config(Config_):
    """The algorithm configuration.

    Attributes:
        kn_num_channels (int): The number of channels for
            :class:`spest.network.KernelNet`.
        kn_kernel_sizes (list[int]): The kernel sizes for each of
            :class:`spest.network.KernelNet` conv weights.
        kernel_length (int): The length of the kernel to estimate.
        kernel_avg_beta (float): The kernel averaging beta for
            :class:`spest.network.KernelNet`.
        lrd_num_convs (int): The number of convolutions in
            :class:`spest.network.LowResDiscriminator`.
        lrd_num_channels (int): The number of channels in the first conv of
            :class:`spest.network.LowResDiscriminator`.
        lrelu_neg_slope (float): The negative slope of leaky ReLU in
            :class:`spest.network.LowResDiscriminator`.

    """
    def __init__(self):
        super().__init__()
        self.add_config('kn_num_channels', 1024)
        self.add_config('kn_num_convs', 6)
        self.add_config('kn_update_step', 1)
        self.add_config('kernel_avg_beta', 0.99)
        self.add_config('kernel_length', 19)
        self.add_config('lrd_num_channels', 64)
        self.add_config('lrelu_neg_slope', 0.1)
        self.add_config('patch_size', 20)
        self.add_config('scale_factor', 1)
        self.add_config('batch_size', 16)
        self.add_config('num_epochs', 30000)
        self.add_config('num_init_epochs', 0)
        self.add_config('smoothness_loss_weight', 1)
        self.add_config('center_loss_weight', 1)
        self.add_config('boundary_loss_weight', 10)
        self.add_config('weight_decay', 0)
        self.add_config('image_save_step', 100)
        self.add_config('eval_step', 100)
        self.add_config('image_save_zoom', 1)
        self.add_config('lrd_kernels', (3, 3, 3, 3, 3))
        self.add_config('learning_rate', 1e-4)
