from actors.repository import ActorRepository


class ActorService:

    def __init__(self):
        self.actor_repsoitory = ActorRepository()

    def get_actors(self):
        return self.actor_repository.get_actors()
    
    def create_actor(self, name, birthday, nationality, biography):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality,
            biography=biography
        )
        return self.actor_repsoitory.create_actor(actor)


