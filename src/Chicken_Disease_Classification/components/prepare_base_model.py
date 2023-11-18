from Chicken_Disease_Classification.entity.config_entity import PrepareBaseModelConfig
import tensorflow as tf
from pathlib import Path

class PrepareBaseModel:
    def __init__ (self, config: PrepareBaseModelConfig):
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.applications.efficientnet.EfficientNetB3(
            include_top = self.config.params_include_top,
            weights = self.config.params_weights,
            input_shape = self.config.params_image_size,
            pooling = 'max'
        )

        self.save_model(path = self.config.base_model_path, model=self.model)

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                layer.trainable = False

        elif (freeze_till is not None) and (freeze_till>0):
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False
        
        full_model = tf.keras.models.Sequential([
            model,
            tf.keras.layers.BatchNormalization(axis= -1, momentum= 0.99, epsilon= learning_rate),
            tf.keras.layers.Dense(256, kernel_regularizer= tf.keras.regularizers.l2(l= 0.016), activity_regularizer= tf.keras.regularizers.l1(0.006), bias_regularizer= tf.keras.regularizers.l1(0.006), activation= 'relu'),
            tf.keras.layers.Dropout(rate= 0.45, seed= 123),
            tf.keras.layers.Dense(classes, activation= 'softmax')
        ])

        full_model.compile(
            optimizer = tf.keras.optimizers.Adamax(learning_rate = learning_rate),
            loss = tf.keras.losses.CategoricalCrossentropy(),
            metrics = ['accuracy']
        )

        full_model.summary()

        return full_model
    
    
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=False,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)