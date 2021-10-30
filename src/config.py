import transformers



MAX_lEN = 128
TRAIN_BATCH_SIZE = 32
VALID_BATCH_SIZE = 8
EPOCHS = 10
BASE_MODEL_PATH = 'roberta-base'
MODEL_PATH = 'model.bin'
TRAINING_FILE = 'ner_dataset.csv'
TOKENIZER = transformers.RobertaTokenizer.from_pretrained(BASE_MODEL_PATH, do_lower_case=True)
