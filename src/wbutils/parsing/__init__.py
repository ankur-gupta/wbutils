from wbutils.framework import set_framework, get_framework, PYTORCH_FRAMEWORK, TENSORFLOW_FRAMEWORK, DEFAULT_FRAMEWORK

FRAMEWORK = get_framework()

if FRAMEWORK == PYTORCH_FRAMEWORK:
    from ._pytorch import CONFIG_ITEMS_FROM_STR, parse_wb_config, get_optimizer_cls, get_loss_cls
elif FRAMEWORK == TENSORFLOW_FRAMEWORK:
    raise NotImplementedError(f'Framework {FRAMEWORK} is not yet implemented')
