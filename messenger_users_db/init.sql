\c messenger-users-db; 

CREATE TABLE IF NOT EXISTS user_data (
    id TEXT PRIMARY KEY,
    login TEXT,
    password TEXT
);

CREATE TABLE IF NOT EXISTS refresh_token_data (
  id TEXT PRIMARY KEY,
  user_id TEXT,
  refresh_token TEXT,
  fingerprint TEXT,
  creation_time INT,
  expiration_time INT,
  CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES user_data(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_user_data ON user_data(id);

CREATE INDEX IF NOT EXISTS idx_tokens ON refresh_token_data(user_id);
