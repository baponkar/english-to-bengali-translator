model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

model.fit(x=train_data, y=train_labels, validation_data=(val_data, val_labels), 
epochs=num_epochs, batch_size=batch_size)

