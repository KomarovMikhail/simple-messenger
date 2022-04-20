\c messenger-main-db; 

CREATE TABLE IF NOT EXISTS chats (
    id TEXT PRIMARY KEY,
    first_user_id TEXT,
    second_user_id TEXT
);

CREATE OR REPLACE FUNCTION create_chat() RETURNS TRIGGER AS $create_chat$
    BEGIN
        EXECUTE format('CREATE TABLE IF NOT EXISTS %I (id TEXT PRIMARY KEY, from_first_user BOOLEAN, send_time INT, message TEXT)', 'chat_' || NEW.id);
        EXECUTE format('CREATE INDEX IF NOT EXISTS idx_%1$s_id ON %1$s(id);', 'chat_' || NEW.id);
        RETURN NULL;
    END;
$create_chat$ LANGUAGE plpgsql;

CREATE TRIGGER on_chat_create_trigger AFTER INSERT ON chats 
    FOR EACH ROW EXECUTE PROCEDURE create_chat();

CREATE OR REPLACE FUNCTION delete_chat() RETURNS TRIGGER AS $delete_chat$
    BEGIN
        EXECUTE format('DROP TABLE IF EXISTS %I CASCADE', 'chat_' || OLD.id);
        RETURN NULL;
    END;
$delete_chat$ LANGUAGE plpgsql;

CREATE TRIGGER on_chat_delete_trigger AFTER DELETE ON chats 
    FOR EACH ROW EXECUTE PROCEDURE delete_chat();

