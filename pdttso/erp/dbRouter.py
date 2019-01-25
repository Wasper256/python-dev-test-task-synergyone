class ErpDBRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'erp':
            return 'erp'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'erp':
            return 'erp'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'erp' and \
           obj2._meta.app_label == 'erp':
           return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'erp':
            if model._meta.app_label == 'erp':
                return True
        elif model._meta.app_label == 'erp':
            return False
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'erp':
            return db == 'erp'
        return None