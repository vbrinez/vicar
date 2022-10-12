class AuthRoter:
    router_app_labels = {'auth', 'contenttypes', 'sessions', 'admin'}

    def db_for_read( self, model, **hints):
        if (model._meta.app_label == 'tienda'):
            return 'tienda'
        return None

    def db_for_write( self, model, **hints):
        if (model._meta.app_label == 'tienda'):
            return 'tienda'
        return None

    def allow_relations(self, obj1, obj2, **hints):
        if (
            obj1._meta_app_label == 'tienda' or
            obj2._meta_app_label == 'tienda'
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if (app_label == 'tienda' ):
            return db == 'tienda'
        return None